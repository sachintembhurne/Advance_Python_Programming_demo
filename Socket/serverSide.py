import socket

host = "localhost"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print("The server is listing for client request on port ", port)
connection, address = s.accept()

print("Connection has been establish from ", str(address))
connection.send("Hello My name is Sachin and i am a server".encode())
connection.close()