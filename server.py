import socket

def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server is listening on {host}:{port}...")

    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    try:
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Msg received from client: {data}")

            if data.strip().lower() == "hello":
                response = "world"
            elif data.strip().lower() == "exit":
                response = "exit"
                conn.sendall(response.encode('utf-8'))
                print("Responding with: exit")
                print("closing connection")
                break
            else:
                response = "Unknown command"

            conn.sendall(response.encode('utf-8'))
            print(f"Responding with: {response}")
    finally:
        conn.close()
        server_socket.close()
        print("Server shutdown successfully.")

if __name__ == "__main__":
    start_server()
