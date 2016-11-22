import socket
import sys


class Client(object):
	def __init__(self,local_ip_address):
		self.local_ip_address = local_ip_address
		self.port = 5000
		self.my_flag = "no"

	def connectionInit(self):
		try:
			self.m_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except Exception as e:
			print(e)
			exit()
		try:
			self.m_socket.connect((self.local_ip_address, self.port))
		except Exception as e:
			print(e)
			exit()



	def beAware(self):
		receiving_b_data = self.m_socket.recv(1024)
		if(receiving_b_data):
			self.my_flag = "yes"
			receiving_utf_data = str(receiving_b_data.decode('ascii'))
			print("\nSERVER : " + receiving_utf_data)
		else:
			self.my_flag = "no"



	def sendMessage(self, string):
		self.m_socket.sendall(bytes(string, 'utf-8'))



	def finish(self):
		self.m_socket.close()

