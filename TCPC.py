import socket

def main():
    host = input("Enter server IP: ")
    port = int(input("Enter server port: "))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        message = input("Enter a string to send: ")
        client_socket.sendall(message.encode())

        data = client_socket.recv(1024)
        print("Reversed string from server:", data.decode())

if __name__ == "__main__":
    main()
