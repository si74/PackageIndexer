#Incredibly Simplified Method of Testing 
#Grabbed a lot of this code from stack overflow and tweaked it
import socket
import time
import threading
 
TCP_IP = '127.0.0.1'
TCP_PORT = 8080
BUFFER_SIZE = 1024

class Connect(object):

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('connecting to host')
        sock.connect((TCP_IP,TCP_PORT))
        return sock

    def send(self, command):
        sock = self.connect()
        recv_data = ""
        data = True

        print('sending: ' + command)
        sock.sendall(command)

        while data:
            data = sock.recv(BUFFER_SIZE)
            recv_data += data 
            print('received: ' + data)

        sock.close()
        return recv_data

if __name__ == "__main__":
	connect = Connect()

	#thoroughly testing glaring errors in commands
	connect.send("STATUS")
	connect.send("STATUS|banana")
	connect.send("REMOVE|banana|hooha")
	connect.send("QUERY|banana|poop")
	connect.send("INDEX|monkey|23haha,")

	connect.send("INDEX|monkey")

    