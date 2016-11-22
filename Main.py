from Client import Client
from Server import Server
import sys
import threading
import time
import random


print("*** chatapp ***")
print("programmer : samanSadeghyan\n")

server = Server()


position = input("choose (server should be started before anything else!):\n1.server \n2.client \n")

my_lock = threading.Lock()

def serverGoToBeAware():
	while True:
		if(server.my_flag == "no"):
			my_lock.release()
		my_lock.acquire()
		server.beAware()
		my_lock.release()
		ran = random.random()
		time.sleep(ran)


def serverCheckSend():
	while True:
		my_lock.acquire()
		i = input("type... ")
		print("YOU : " + i)
		server.sendMessage(i)
		my_lock.release()
		ran = random.random()
		time.sleep(ran)



def clientGoToBeAware():
	while True:
		if(client.my_flag == "no"):
			my_lock.release()
		my_lock.acquire()
		client.beAware()
		my_lock.release()
		ran = random.random()
		time.sleep(ran)


def clientCheckSend():
	while True:
		my_lock.acquire()
		i = input("type... ")
		print("YOU : " + i)
		client.sendMessage(i)
		my_lock.release()
		ran = random.random()
		time.sleep(ran)


if(position == "1"): ###------- server
	server.connectionInit()
	server.listen()

	my_thread_2 = threading.Thread(target = serverCheckSend)
	my_thread_2.start()


	my_thread_1 = threading.Thread(target = serverGoToBeAware)
	my_thread_1.start()


	pos = "server"


elif(position == "2"): ###------ client
	
	ip = input("please enter server's ip address : \n")

	client = Client(ip)

	client.connectionInit()

	my_thread_2 = threading.Thread(target = clientCheckSend)
	my_thread_2.start()
	
	my_thread_1 = threading.Thread(target = clientGoToBeAware)
	my_thread_1.start()

	

	pos = "client"

else:
	print("wrong input!!!")
	exit()



my_thread_1.join()
my_thread_2.join()

if(pos == "server"):
	server.finish()
elif(pos == "client"):
	client.finish()










