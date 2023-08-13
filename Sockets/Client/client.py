import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connecting_to_server(self):
        self.client.connect((self.host, self.port))
        print('We are connected!\n')

    def sending_file(self, file1):
        self.client.send(file1.encode())
        with open(file1, 'rb') as file:
            for data in file.readlines():
                self.client.send(data)
        print('File uploaded successfully!')

    def closing_connection(self):
        self.client.close()

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 9999

    client = Client(HOST, PORT)
    client.connecting_to_server()
    file = str(input('Insert the file >>'))
    client.sending_file(file)
    client.closing_connection()