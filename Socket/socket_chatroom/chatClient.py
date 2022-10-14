from tkinter import *
import tkinter
import socket
from threading import Thread


def receive():
    while True:
        try:
            message = s.recv(1024).decode("utf8")
            message_list.insert(tkinter.END, message)
        except:
            print("There is an error while receiving a message")
            break


def send():
    message = my_message.get()
    my_message.set("")
    s.send(bytes(message, "utf8"))

    if message == "#quit":
        s.close()
        window.quit()


def on_closing():
    my_message.set("#quit")
    send()


window = Tk()
window.title("Chat Room")
window.configure(bg="green")
messages_frame = Frame(window, height=100, width=100, bg="red")
my_message = StringVar()
my_message.set("")

scroll_bar = Scrollbar(messages_frame)
message_list = Listbox(messages_frame, height=15, width=100, bg="red", yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
message_list.pack(side=LEFT, fill=BOTH)
messages_frame.pack()

button_label = Label(window, text="Enter your message", fg="blue", font="Areial", bg="red")
button_label.pack()

entry_field = Entry(window, textvariable=my_message, fg="red", width=50)
entry_field.pack()

send_button = Button(window, text="Send", bg="green", font="Aerial", fg="white", command=send)
send_button.pack()

quit_button = Button(window, text="Quit", bg="green", font="Aerial", fg="white", command=on_closing)
quit_button.pack()

window.protocol("WM_DELETE_WINDOW", on_closing)

Host = "127.0.0.1"
Port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, Port))

receive_thread = Thread(target=receive)
receive_thread.start()

mainloop()
