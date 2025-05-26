import socket

def start_client(host='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    try:
        while True:
            msg = input("Msg to send: ").strip()
            client_socket.sendall(msg.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Server responded with: {response}")

            if msg.lower() == "exit":
                print("closing connection")
                break
    finally:
        client_socket.close()
        print("Client shutdown successfully.")

if __name__ == "__main__":
    start_client()
