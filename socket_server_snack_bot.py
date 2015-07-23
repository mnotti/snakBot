import SocketServer

class TCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print "connected to : ", self.client_address[0]
		while 1:
			self.reqdata = self.request.recv(1024).strip()
			print "Packet received: ", self.reqdata
	#def update(self):
	#	while 1:
	#		self.request.sendall("updates...")

if __name__ == "__main__":
	HOST, PORT = 'localhost', 6969
	server = SocketServer.TCPServer((HOST, PORT), TCPHandler)
	print "Listening"
	server.serve_forever()



