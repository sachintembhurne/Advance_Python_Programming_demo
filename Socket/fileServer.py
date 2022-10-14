import socket

host = "localhost"
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

print("The server is listening for client request on port ", port)
connection, address = s.accept()
print("Connection has been establish from ", str(address))
try:
    fileName = connection.recv((1024))
    file = open(fileName, 'rb')
    readFile = file.read()
    connection.send(readFile)
    file.close()
    connection.close()
except:
    connection.send("File is not found on server".encode())

