import socket

# CREATING AN OBJECT OF THE SOCKET
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# CONNECTION TO A SERVER HOST & PORT
host = socket.gethostname()
port = 2347

# CONNECTING TO THE SERVER
conn.connect((host, port))

# SENDING A MESSAGE
while True:
    msg = input("Message: ")
    conn.send(msg.encode("utf-8"))
    if (msg == "exit"):
        break

# CLOSING THE CONNECTION
conn.close()
