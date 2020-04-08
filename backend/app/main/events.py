from flask import current_app as app
from .room import Room
from .config_helper import get_dict_instance_by_lang
from functools import wraps
from loguru import logger
from flask import request
from flask_socketio import emit, join_room, leave_room
from .. import socket_io

rooms = {}
rooms_names_dict = {
    lang: get_dict_instance_by_lang(lang) for lang in app.config['DEFAULT_DICT']
}
user_by_sid = {}
room_by_user = {}


def updates_state(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"request {args}, {kwargs}")
        try:
            user = user_by_sid[request.sid]
        except KeyError:
            logger.error("Unregistered user attempted a request.")
            return

        room = None
        try:
            room = rooms[room_by_user[user]]
        except KeyError:
            logger.warning(f"User {user} is not associated with any room.")

        if room:
            logger.info(f"State change request by {user} in room {room.name}.")
        else:
            logger.info(f"State change request by {user}.")

        func(user, room, *args, **kwargs)

        if room and len(room.online()) == 0:
            logger.info(f"Room {room.name} is now empty. Cleaning the trash.")
            rooms_names_dict[room.lang].add_word(room, 1)
            rooms[room] = None
        if not room:
            try:
                room = rooms[room_by_user[user]]
            except KeyError:
                logger.warning(f"Could not find associated room even after the state change.")
        if room:
            broadcast = room.get_broadcast_data()
            logger.debug("Broadcasting data...")
            logger.debug(broadcast)
            emit('update', broadcast, room=room.name)
    return wrapper


def register_user(func):
    @wraps(func)
    def wrapper(data, *args, **kwargs):
        user_by_sid[request.sid] = data['username']
        logger.info(f"New user with sid f{request.sid} is now associated with {data['username']}")
        func(data, *args, **kwargs)
    return wrapper


@socket_io.on('connect')
def on_connect():
    logger.info(f'New connection appeared. SID: {request.sid}')


@socket_io.on('disconnect')
@updates_state
def on_disconnect(user, room):
    room.leave(user)
    logger.info('User disconnected.')


@socket_io.on('create')
@register_user
@updates_state
def on_create(user, _, data):
    name = rooms_names_dict[data['lang']].pop_random_word()
    rooms[name] = Room(name, user, data['lang'])
    room_by_user[user] = name
    join_room(name)
    logger.info(f"User created new room called {name}")


@socket_io.on('join')
@register_user
@updates_state
def on_join(user, _, data):
    room = rooms[data['room']]
    room_by_user[user] = room.name
    join_room(room.name)
    room.join(user)
    logger.info(f"User joined room called {room.name}")


@socket_io.on('leave')
@updates_state
def on_leave(user, room):
    room.make_offline(user)
    leave_room(room.name)
    logger.info(f"User left room.")


@socket_io.on("init")
@updates_state
def on_init(_, room, data):
    room.start_game(data['settings'])
    logger.info(f"User started new game.")


@socket_io.on("start_round")
@updates_state
def on_start_round(_user, room):
    room.start_round()
    logger.info(f"User started new round.")


@socket_io.on("end_round")
@updates_state
def on_end_round(_user, room):
    room.finish_round()
    logger.info(f"User finished current round.")


@socket_io.on("remove_word")
@updates_state
def on_remove_word(_user, room, data):
    room.remove_word(data['verdict'], data['screen_time'])
    logger.info(f"User removed word with result {data['verdict']}. Last screen time {data['screen_time']}.")


@socket_io.on("endgame")
@updates_state
def on_endgame(_user, room):
    room.endgame()
    logger.info(f"User ended current game.")
