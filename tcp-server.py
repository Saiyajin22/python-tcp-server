import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
# we tell the server to start listening with
# a maximum backlog of connections set to 5
server.listen(10)

print(f"[+] Listening on port {bind_ip} : {bind_port}")


def handle_client(client_socket: socket.socket):
    chunks = []
    while True:
        chunk = client_socket.recv(4096)  # Read in 4KB blocks
        if not chunk:
            print("breaked")
            break  # Client closed the connection (EOF)
        chunks.append(chunk)

    request = b"".join(chunks)
    try:
        # Try to print as clean text
        print(request.decode('utf-8'))
    except UnicodeDecodeError:
        # Fallback: print the raw bytes if it contains non-text/binary data
        print(request)
    client_socket.send(request)
    client_socket.close()


while True:
    # When a client connects we receive the
    # client socket into the client variable, and
    # the remote connection details into the addr variable
    client, addr = server.accept()
    print(f"[+] Accepted connection from: {addr[0]}:{addr[1]}")
    # spin up our client thread to handle the incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
