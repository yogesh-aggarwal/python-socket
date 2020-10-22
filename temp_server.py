import socket

# CREATING AN OBJECT OF THE SOCKET
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# BINDING THE CONNECTION TO A SPECIFIC HOST & PORT
# host = socket.gethostname()
host = socket.gethostbyname('www.google.com')
port = 2347
conn.bind((host, port))

# WAITING FOR THE CONNECTION
print("Waiting for connection...")
conn.listen(5)

# ACCEPTING THE CLIENT REQUEST
client, address = conn.accept()
print(f"Connected: {address}")

# RECIEVING THE MESSAGE
while True:
    msg = client.recv(1024).decode("utf-8")
    print(f"Recieved: {msg}")
    if (msg == "exit"):
        break

# CLOSING THE CONNECTION
conn.close()
