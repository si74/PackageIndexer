import re
import SocketServer
from packageGraph import PackageGraph
#instantiate global graph object 
graph = PackageGraph()

class MyTCPHandler(SocketServer.BaseRequestHandler):
    
    #variables accessible by the class
    COMMANDS = ['INDEX','REMOVE','QUERY']
    identifier = re.compile(r"^[^\d\W]\w*\Z", re.UNICODE)

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()

        print "{} wrote:".format(self.client_address[0])
        print self.data

        result = self.analyzeRequest(self.data)
        print result

        # just send back the same data, but upper-cased
        self.request.sendall(result)

    def parseMessage(self,message):

    	split_msg = message.rstrip("\n").split('|')
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

    	#try attempting actions
    	if cleanedMessage[0] == 'INDEX':
    		result = graph.addPackage(cleanedMessage[1],cleanedMessage[2])
    	elif cleanedMessage[0] == 'REMOVE':
    		result = graph.removePackage(cleanedMessage[1])
    	elif cleanedMessage[0] == 'QUERY':
    		result = graph.getPackage(cleanedMessage[1])

    	return "FAIL\n" if not result else "OK\n" 


if __name__ == "__main__":
    HOST, PORT = "127.0.01", 8080
    SocketServer.TCPServer.allow_reuse_address = True
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    server.serve_forever()