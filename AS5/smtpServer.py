import socket

class SMTPServer:
    def __init__(self):
        self.session = {}

    def handle_client(self, client_socket):
        client_socket.sendall(b'220 Welcome to My SMTP Server\r\n')
        client_message = client_socket.recv(1024).decode()
        print(f"Client message: {client_message}")

        while True:
            if client_message.startswith('QUIT'):
                client_socket.sendall(b'221 Bye\r\n')
                client_socket.close()
                break
            elif client_message.startswith('HELO'):
                client_socket.sendall(b'250 Hello\r\n')
            elif client_message.startswith('MAIL FROM'):
                client_socket.sendall(b'250 OK\r\n')
            elif client_message.startswith('RCPT TO'):
                client_socket.sendall(b'250 OK\r\n')
            elif client_message.startswith('DATA'):
                client_socket.sendall(b'354 Start mail input; end with <CRLF>.<CRLF>\r\n')
                # Receive email message
                email_data = b''
                while True:
                    data = client_socket.recv(1024)
                    if data == b'.\r\n':
                        break
                    email_data += data
                print("Received email data:")
                print(email_data.decode())
                client_socket.sendall(b'250 OK\r\n')
            else:
                client_socket.sendall(b'500 Command unrecognized\r\n')

            client_message = client_socket.recv(1024).decode()

    def main(self):
        host = 'localhost'
        port = 25

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen()
            print(f"Server listening on {host}:{port}")

            while True:
                client_socket, client_address = server_socket.accept()
                print(f"Connection accepted from {client_address}")

                self.handle_client(client_socket)

if __name__ == "__main__":
    server = SMTPServer()
    server.main()
