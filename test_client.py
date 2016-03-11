#Incredibly Simplified Method of Testing 
#Grabbed a lot of this code from stack overflow and tweaked it
import socket
import time
import threading
import asyncore
 
# TCP_IP = '127.0.0.1'
# TCP_PORT = 8080
# BUFFER_SIZE = 1024

# class Connect(object):

#     def connect(self):
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         print('connecting to host')
#         sock.connect((TCP_IP,TCP_PORT))
#         return sock

#     def send(self, command):
#         sock = self.connect()
#         recv_data = ""
#         data = True

#         print('sending: ' + command)
#         sock.sendall(command)

#         while data:
#             data = sock.recv(BUFFER_SIZE)
#             recv_data += data 

#         sock.close()
#         print recv_data
#         return recv_data

# if __name__ == "__main__":
# 	connect = Connect()

# 	#thoroughly testing glaring errors in commands
# 	assert(connect.send("STATUS") == "ERROR\n"), "not a legitimate command"
# 	print 'HERE'
# 	assert(connect.send("STATUS|banana") == "ERROR\n"), "still not a legitimate command"
# 	assert(connect.send("REMOVE|banana|hooha") == "ERROR\n"), "still not a legitimate command"
# 	assert(connect.send("QUERY|banana|poop") == "ERROR\n"), "can't have dependencies here bozo"
# 	assert(connect.send("INDEX|monkey|23haha,") == "ERROR\n"), "not valid identifier for package"

# 	#testing more intense situations
# 	#Testing indexing
# 	assert(connect.send("INDEX|monkey") == "OK\n"), "should be able to add"
# 	assert(connect.send("INDEX|monkey") == "FAIL\n"), "can't add this shit twice"
# 	assert(connect.send("INDEX|kitten|monkey,tuna,") == "FAIL\n"), "dependent package not added"
# 	assert(connect.send("INDEX|tuna") == "OK\n"), "should be able to add"
# 	assert(connect.send("INDEX|kitten|monkey,tuna,") == "OK\n"), "dependencies good so should work"

# 	#Testing queries
# 	assert(connect.send("QUERY|dog") == "FAIL\n"), "hasn't been added so should fail"
# 	assert(connect.send("QUERY|kitten") == "OK\n"), "hasn't been added so should fail"

# 	#Testing removaln
# 	assert(connect.send("REMOVE|monkey") == "FAIL\n"), "packages still dependent on this"
# 	assert(connect.send("REMOVE|tuna") == "FAIL\n"), "packages still dependent on this"
# 	assert(connect.send("REMOVE|kitten") == "OK\n"), "can easily remove"
# 	assert(connect.send("REMOVE|monkey") == "OK\n"), "can finally remove now"
	
# 	connect.send("REMOVE|avce00|")

class Client(asyncore.dispatcher_with_send):
    def __init__(self, host, port, message):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.out_buffer = message

    def handle_close(self):
        self.close()

    def handle_read(self):
    	result = self.recv(1024)
        print 'Received', result
        return result
        self.close()

if __name__ == "__main__":
	c = Client('localhost', 8080, 'Hello, world')
	Client('localhost', 8080, 'REMOVE|avce00|')
	Client('localhost', 8080, 'REMOVE|avce00|')
	Client('localhost', 8080, 'INDEX|monkey')
	asyncore.loop()
    