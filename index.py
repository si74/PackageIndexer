# import socket
# import threading
# import time

# #important variables
# TCP_IP = '127.0.01'
# TCP_PORT = 8080
# BUFFER_SIZE = 1024

# #ATTEMPT 1- USING SOCKETS
# import socket
# from threading import Thread
# from SocketServer import ThreadingMixIn
 
# class ClientThread(Thread):
 
#     def __init__(self,ip,port):
#         Thread.__init__(self)
#         self.ip = ip
#         self.port = port
#         print "[+] New thread started for "+ip+":"+str(port)
 
 
#     def run(self):
#         while True:
#             data = conn.recv(2048)
#             if not data: break
#             print "received data:", data
#             conn.send(data)  # echo
 
# TCP_IP = '0.0.0.0'
# TCP_PORT = 62
# BUFFER_SIZE = 20  # Normally 1024, but we want fast response
 
 
# tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# tcpsock.bind((TCP_IP, TCP_PORT))
# threads = []
 
# while True:
#     tcpsock.listen(4)
#     print "Waiting for incoming connections..."
#     (conn, (ip,port)) = tcpsock.accept()
#     newthread = ClientThread(ip,port)
#     newthread.start()
#     threads.append(newthread)
 
# for t in threads:
#     t.join()

# #ATTEMPT 2 -

# #!/usr/bin/env python 

# """ 
# An echo server that uses threads to handle multiple clients at a time. 
# Entering any line of input at the terminal will exit the server. 
# """ 

# import select 
# import socket 
# import sys 
# import threading 

# class Server: 
#     def __init__(self): 
#         self.host = '' 
#         self.port = 50000 
#         self.backlog = 5 
#         self.size = 1024 
#         self.server = None 
#         self.threads = [] 

#     def open_socket(self): 
#         try: 
#             self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#             self.server.bind((self.host,self.port)) 
#             self.server.listen(5) 
#         except socket.error, (value,message): 
#             if self.server: 
#                 self.server.close() 
#             print "Could not open socket: " + message 
#             sys.exit(1) 

#     def run(self): 
#         self.open_socket() 
#         input = [self.server,sys.stdin] 
#         running = 1 
#         while running: 
#             inputready,outputready,exceptready = select.select(input,[],[]) 

#             for s in inputready: 

#                 if s == self.server: 
#                     # handle the server socket 
#                     c = Client(self.server.accept()) 
#                     c.start() 
#                     self.threads.append(c) 

#                 elif s == sys.stdin: 
#                     # handle standard input 
#                     junk = sys.stdin.readline() 
#                     running = 0 

#         # close all threads 

#         self.server.close() 
#         for c in self.threads: 
#             c.join() 

# class Client(threading.Thread): 
#     def __init__(self,(client,address)): 
#         threading.Thread.__init__(self) 
#         self.client = client 
#         self.address = address 
#         self.size = 1024 

#     def run(self): 
#         running = 1 
#         while running: 
#             data = self.client.recv(self.size) 
#             if data: 
#                 self.client.send(data) 
#             else: 
#                 self.client.close() 
#                 running = 0 

# if __name__ == "__main__": 
#     s = Server() 
#     s.run()

#ATTEMPT 3 - 
#APPROACH TO THIS
import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "127.0.01", 8080

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()


#Ensure message sent is of the correct format using regex
#<command>|<package>|<dependencies>

#ensure that the command is legitimate


#