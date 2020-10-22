import socket


HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode()
    msgLength = len(message)
    sendLength = str(msgLength).encode(FORMAT)
    sendLength += b" "*(HEADER - len(sendLength))
    client.send(sendLength)
    client.send(message)
    print(client.recv(4096).decode(FORMAT))


send("Hey!")
send("Hey!")
send("Hey!")

send(DISCONNECT_MESSAGE)
