import socket
from threading import Thread

clients = {}
addresses = {}

Host = "127.0.0.1"
Port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Host, Port))


def accept_client_connections():
    while True:
        client_connection, client_address = s.accept()
        print(client_address, "Has connected")
        client_connection.send("Welcome to the chat room! Please type your name to continue".encode("utf8"))
        addresses[client_connection] = client_address
        Thread(target=handle_client, args=(client_connection, client_address)).start()


def broadcast(message, prefix=""):
    for x in clients:
        x.send(bytes(prefix, "utf8") + message)


def handle_client(connection, address):
    name = connection.recv(1024).decode("utf8")
    welcome = "Welcome " + name + " You can type #quite if you want to leave the chat room"
    connection.send(bytes(welcome, "utf8"))

    message = name + " has recently joined the chat room"
    broadcast(bytes(message, "utf8"))
    clients[connection] = name
    while True:
        message = connection.recv(1024)

        if message != bytes("#quit", "utf8"):
            broadcast(message, name + ":")

        else:
            connection.send(bytes("#quite", "utf8"))
            connection.close()
            del clients[connection]
            broadcast(bytes(name + " Has left the chat room","utf8"))


if __name__ == "__main__":
    s.listen(5)
    print("The server has been started and is now listening to clients requests")
    t1 = Thread(target=accept_client_connections)
    t1.start()
    t1.join()
