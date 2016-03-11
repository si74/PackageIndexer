import re
import socket
import threading
import SocketServer
from packageGraph import PackageGraph
import logging

#instantiate global graph object 
graph = PackageGraph()
#threadlock for shared graph resource
threadLock = threading.Lock()

#have logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# class MyTCPHandler(SocketServer.BaseRequestHandler):
    
#     #variables accessible by the class
#     COMMANDS = ['INDEX','REMOVE','QUERY']
#     identifier = re.compile(r"^[^\d\W]\w*\Z", re.UNICODE)

#     def handle(self):

#         print self.request.recv(1024)

#         # self.request is the TCP socket connected to the client
#         self.data = self.request.recv(1024).strip()
#         cur_thread = threading.current_thread()

#         response = "{} : {}".format(cur_thread.name, self.data)
#         print response

#         #result = self.analyzeRequest(self.data)
#         #print result

#         # just send back the same data, but upper-cased
#         self.request.sendall(response)

#     def parseMessage(self,message):

#     	split_msg = message.rstrip("\n").rstrip('|').split('|')
#     	msg = map(lambda x: x.strip(" "), split_msg) #a bit forgiving of trailing whitespace

#     	#if insufficient commands or incorrect commands
#     	if (len(msg) not in [2,3] or msg[0] not in self.COMMANDS): return False
    	
#     	#for query or remove, dependencies should NOT be given
#     	if (msg[0] in ['REMOVE','QUERY'] and len(msg) > 2): return False

#     	#for index, if dependencies given, ensure the dependencies are of the correct structure
#     	dependencies = []
#     	if (msg[0] == 'INDEX' and len(msg) == 3):
#     			dependencies = msg[2].rstrip(",").split(',') #a bit forgiving to trailing commas
#     			for d in dependencies:
#     				if not self.validIdentifier(d): return False

#     	return [msg[0],msg[1],dependencies]

#     def validIdentifier(self,string):
#     	return (re.match(self.identifier, string) is not None)

#     def analyzeRequest(self, message):

#     	#first ensure that the message is of the correct format
#     	cleanedMessage = self.parseMessage(message)
#     	if not cleanedMessage: return "ERROR\n"

#         #lock thread b/c we are accessing graph
#         #threadLock.acquire()
#     	#try attempting actions
#     	if cleanedMessage[0] == 'INDEX':
#     		result = graph.addPackage(cleanedMessage[1],cleanedMessage[2])
#     	elif cleanedMessage[0] == 'REMOVE':
#     		result = graph.removePackage(cleanedMessage[1])
#     	elif cleanedMessage[0] == 'QUERY':
#     		result = graph.getPackage(cleanedMessage[1])

#         #unlock thread b/c we are done accessing graph
#         #threadLock.release()

#     	return "FAIL\n" if not result else "OK\n" 

# class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    
#     timeout = 3
#     daemon_threads = True
#     allow_reuse_address = True

#     def __init__(self, server_address, RequestHandlerClass):
#         SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass)

# if __name__ == "__main__":
#     HOST, PORT = "127.0.01", 8080
#     server = ThreadedTCPServer((HOST, PORT), MyTCPHandler)
#     server.serve_forever()

#TRYING SOME OTHER SHIT
import asyncore
import socket

class EchoHandler(asyncore.dispatcher_with_send):

    COMMANDS = ['INDEX','REMOVE','QUERY']
    identifier = re.compile(r"^[^\d\W]\w*\Z", re.UNICODE)
    
    def handle_read(self):
        data = self.recv(8192)
        if data:
            print data
            result = self.analyzeRequest(data)
            print result
            self.send(result)

    def parseMessage(self,message):

      split_msg = message.rstrip("\n").rstrip('|').split('|')
      msg = map(lambda x: x.strip(" "), split_msg) #a bit forgiving of trailing whitespace

      #if insufficient commands or incorrect commands
      if (len(msg) not in [2,3] or msg[0] not in self.COMMANDS): return False
        
      #for query or remove, dependencies should NOT be given
      if (msg[0] in ['REMOVE','QUERY'] and len(msg) > 2): return False

      #for index, if dependencies given, ensure the dependencies are of the correct structure
      dependencies = []
      if (msg[0] == 'INDEX' and len(msg) == 3):
              dependencies = msg[2].rstrip(",").split(',') #a bit forgiving to trailing commas
              for d in dependencies:
                  if not self.validIdentifier(d): return False

      return [msg[0],msg[1],dependencies]

    def validIdentifier(self,string):
      return (re.match(self.identifier, string) is not None)

    def analyzeRequest(self, message):

      #first ensure that the message is of the correct format
      cleanedMessage = self.parseMessage(message)
      if not cleanedMessage: return "ERROR\n"

        #lock thread b/c we are accessing graph
        #threadLock.acquire()
      #try attempting actions
      if cleanedMessage[0] == 'INDEX':
          result = graph.addPackage(cleanedMessage[1],cleanedMessage[2])
      elif cleanedMessage[0] == 'REMOVE':
          result = graph.removePackage(cleanedMessage[1])
      elif cleanedMessage[0] == 'QUERY':
          result = graph.getPackage(cleanedMessage[1])

        #unlock thread b/c we are done accessing graph
        #threadLock.release()

      return "FAIL\n" if not result else "OK\n" 

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = EchoHandler(sock)

server = EchoServer('localhost', 8080)
asyncore.loop()