import socket
import thread
import subprocess
import pdb
import multiprocessing

def handleConnection(message):
	print message

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 6968

s.bind((host, port))
print 'listening...'

s.listen(10)
connection, addr = s.accept()
while 1:
	message = connection.recv(1024)
	print message
	filename="connectionOut.txt"
	f=open(filename, "a")
	f.write(message)
	f.close()
	
connection.close()
