import socket

target_host = "localhost"
target_port = 9999

#creating socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connecting the client
client.connect((target_host, target_port))
#sending data
client.send("hello".encode())
# tell the server we are done sending, sending EOF
client.shutdown(socket.SHUT_WR)
#receiving the data 
response = client.recv(4096)
print(response.decode())