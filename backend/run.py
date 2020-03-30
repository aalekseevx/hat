from flask import Flask, request
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from room import Room
import random
import string
from dictionary import Dictionary


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sample_secret'
socketio = SocketIO(app, cors_allowed_origins='*')


class RoomDictionary:
    def __init__(self):
        pass

    def pop_random_word(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


rooms = {}
rooms_names_dict = RoomDictionary()
users_by_sid = {}
room_by_users = {}


def create_room(username):
    name = rooms_names_dict.pop_random_word()
    rooms[name] = Room(name, username)
    return name, rooms[name].get_broadcast_data()


@socketio.on('disconnect')
def on_disconnect():
    user = users_by_sid[request.sid]
    room = room_by_users[user]
    rooms[room].leave(user)
    print("Disconnect ", request.sid)
    emit('update', rooms[room].get_broadcast_data(), room=room)


@socketio.on('create')
def on_create(data):
    users_by_sid[request.sid] = data['username']
    name, room = create_room(data['username'])
    room_by_users[data['username']] = name
    join_room(name)
    emit('update', room, room=name)


@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    users_by_sid[request.sid] = data['username']
    room_by_users[username] = room
    join_room(room)
    rooms[room].join(username)
    emit('update', rooms[room].get_broadcast_data(), room=room)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = room_by_users[username]
    rooms[room].make_offline(username)
    leave_room(room)
    emit('update', rooms[room].get_broadcast_data(), room=room)


@socketio.on("init")
def on_init(data):
    print(data)
    username = data['username']
    room = room_by_users[username]
    rooms[room].start_game(data['settings'])
    emit('update', rooms[room].get_broadcast_data(), room=room)


@socketio.on("start_round")
def on_start_round():
    user = users_by_sid[request.sid]
    room = room_by_users[user]
    rooms[room].start_round()
    emit('update', rooms[room].get_broadcast_data(), room=room)


@socketio.on("end_round")
def on_end_round():
    user = users_by_sid[request.sid]
    room = room_by_users[user]
    rooms[room].finish_round()
    emit('update', rooms[room].get_broadcast_data(), room=room)


@socketio.on("remove_word")
def on_remove_word(result):
    user = users_by_sid[request.sid]
    room = room_by_users[user]
    rooms[room].remove_word(result)
    emit('update', rooms[room].get_broadcast_data(), room=room)


@socketio.on("endgame")
def on_endgame():
    user = users_by_sid[request.sid]
    room = room_by_users[user]
    rooms[room].endgame()
    emit('update', rooms[room].get_broadcast_data(), room=room)


@app.route('/')
def hello_world():
    return "Hello, world"


if __name__ == '__main__':
    socketio.run(app, debug=True)
