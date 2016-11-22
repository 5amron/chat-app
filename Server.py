import socket
import sys



class Server(object):
	def __init__(self):
		self.local_ip_address = socket.gethostname()
		self.port = 5000
		self.my_flag = "no"



	def connectionInit(self):
		try:
			self.m_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except Exception as e:
			print(e)
			exit()
		try:
			self.m_socket.bind((self.local_ip_address, self.port))
		except Exception as e:
			print(e)
			exit()
		

		
	def listen(self):
		self.m_socket.listen(5)
		print("server is listening on : "+ str(socket.gethostbyname(self.local_ip_address))+ ":" + str(self.port))
		while True:
		    self.conn, self.client_addr = self.m_socket.accept()
		    print("client :::: "+ str(self.client_addr) + " connected ")
		    if self.conn:
		    	break



	def beAware(self):
		receiving_b_data = self.conn.recv(1024)
		if(receiving_b_data):
			self.my_flag = "yes"
			receiving_utf_data = str(receiving_b_data.decode('ascii'))
			print("\nCLIENT : " + receiving_utf_data)
		else:
			self.my_flag = "no"



	def sendMessage(self, string):
		self.conn.sendall(bytes(string, 'utf-8'))


	def finish(self):
		self.conn.close()
		self.m_socket.close()

