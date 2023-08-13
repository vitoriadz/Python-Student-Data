import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))

    def starting_connection(self):
        print('Waiting for connections!\n')
        self.server.listen(1)
        connection, address = self.server.accept()
        receiving_file(connection)
        self.server.close()


def receiving_file(connection):
    file = connection.recv(3000000).decode()
    with open(file, 'wb') as file:
        while True:
            data = connection.recv(3000000)
            if not data:
                print('Closing connection!')
                break
            file.write(data)
    print(f'File {file} received without problems!\n')


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 9999

    server = Server(HOST, PORT)
    server.starting_connection()