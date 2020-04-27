from app.app_factory import create_app
if __name__ == '__main__':
    create_app()
    from app.app_factory import socket_io
    socket_io.run(create_app(), debug=True, host='127.0.0.1')
