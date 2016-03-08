import socket

#important variables
TCP_IP = '127.0.01'
TCP_PORT = 8080
BUFFER_SIZE = 1024
MAX_THREADS = 

if __name__ == "__main__":
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((TCP_IP, TCP_PORT))
	s.listen(1)
 
	conn, addr = s.accept()
	print 'Connection address:', addr
	
	while 1:
     	data = conn.recv(BUFFER_SIZE)
     	if not data: break
     	print "received data:", data
     	conn.send(data)  # echo
		conn.close()

#Ensure message sent is of the correct format using regex
#<command>|<package>|<dependencies>

#ensure that the command is legitimate


#