import socket
import sys
from lab6.server.handler import Handler


class Server:
    HOST = ''
    PORT = 1235

    def __init__(self):
        self.handler = Handler()

    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Created socket')

        try:
            s.bind((self.HOST, self.PORT))
        except socket.error as msg:
            print('Bind failed. Error Code : ' + str(msg.errno) + ' Message ' + msg.strerror)
            sys.exit()

        print('Socket bind complete')
        s.listen(3)
        print('Socket is listening...')

        while True:
            conn, addr = s.accept()
            self.handler.handle(conn)


if __name__ == '__main__':
    server = Server()
    server.start()

