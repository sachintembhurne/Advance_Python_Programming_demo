import threading
from threading import Thread
from time import sleep
from threading import *


# t = threading.current_thread().getName()
# if threading.current_thread() == threading.main_thread():
#     for x in range(10):
#         if x %2 == 0:
#             print(x)
# else:
#     print("The running thread is not a Main Thread")
# print(t)

# #------------------------------------------------
#
# threading.current_thread().name = "Sachin"
# print(threading.current_thread().name)
#
# #---------------------------------------------------
#
# def evenNumber():
#     for x in range(20):
#         if x % 2 == 0:
#             print(x)
#     a=threading.current_thread().name
#     print(a)
#
# t = Thread(target=evenNumber())
# t.start()
#
# #----------------------------------------
#
# def even_odd():
#     evenNumber()
#     print(threading.current_thread().name)
#     oddNumber()
#
#
# def evenNumber():
#     print("even numbers are\n")
#     for x in range(10):
#         if x % 2 == 0:
#             print(x)
#
#
# def oddNumber():
#     print("odd numbers are\n")
#     for x in range(10):
#         if x % 2 != 0:
#             print(x)
#
#
# t = Thread(target=even_odd, name="even_odd")
# #t1 = Thread(target=even_odd, name="even_odd")
# t.start()

# ----------------------------------------
#
# class MyThread(Thread):
#     def run(self):
#         print("Pyramid")
#         print(threading.current_thread().name)
#         for x in range(0,5):
#             for j in range(0, x+1):
#                 print("*", end=" ")
#             print("\r")
#
# obj = MyThread()
# obj.start()
#
# #---------------------------------------------
#
# class MyThread:
#     def naturalNo(self):
#         if threading.current_thread().name == "Thread-1":
#             for x in range(10):
#                 print(x)
#         else:
#             print("This is not Thread-1")
#
#
# obj = MyThread()
# t = Thread(target=obj.naturalNo)
# t.start()
#
# #---------------------------------------------------
#
# def naturalNo():
#     print(threading.current_thread().name,"Has Started")
#     sleep(2)
#     for x in range (10):
#         print(x)
#
#     print(threading.current_thread().name, "Has Ended")
#
#
# t1 = Thread(target=naturalNo)
# t2 = Thread(target=naturalNo)
# t3 = Thread(target=naturalNo)
# t4 = Thread(target=naturalNo)
# t5 = Thread(target=naturalNo)
#
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
#
# #-----------------------------------------
#
# class FlightReservation:
#     l = Lock()
#
#     def __init__(self, ticket_left):
#         self.ticket_left = ticket_left
#
#     l.acquire()
#
#     def buy(self, ticketRequested):
#
#         if self.ticket_left >= ticketRequested:
#             print("Your Tickets is confirmed")
#             print("Please make a payment and take your ticket")
#             self.ticket_left -= ticketRequested
#         else:
#             print("There is not enough tickets remaining")
#
#     l.release()
#
#
# obj = FlightReservation(15)
# t1 = Thread(target=obj.buy, args=[3])
# t2 = Thread(target=obj.buy, args=[4])
# t3 = Thread(target=obj.buy, args=[3])
# t4 = Thread(target=obj.buy, args=[5])
# t1.start()
# t2.start()
# t3.start()
# t4.start()

#-----------------------------------------

class FlightReservation:
    l = Semaphore()

    def __init__(self, ticket_left):
        self.ticket_left = ticket_left

    l.acquire()

    def buy(self, ticketRequested):

        if self.ticket_left >= ticketRequested:
            print("Your Tickets is confirmed")
            print("Please make a payment and take your ticket")
            self.ticket_left -= ticketRequested
        else:
            print("There is not enough tickets remaining")

    l.release()


obj = FlightReservation(15)
t1 = Thread(target=obj.buy, args=[3])
t2 = Thread(target=obj.buy, args=[4])
t3 = Thread(target=obj.buy, args=[3])
t4 = Thread(target=obj.buy, args=[5])
t1.start()
t2.start()
t3.start()
t4.start()