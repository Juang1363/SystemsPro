import socket

def reverse_string(s):
    return s[::-1]

def main():
    host = "0.0.0.0"
    port = int(input("Enter port to listen on: "))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on port {port}...")

        client_socket, addr = server_socket.accept()
        with client_socket:
            print(f"Client connected: {addr}")
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                reversed_data = reverse_string(data.decode())
                client_socket.sendall(reversed_data.encode())
            print("Client disconnected.")

if __name__ == "__main__":
    main()
