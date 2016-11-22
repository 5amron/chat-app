import os
import subprocess
import sys

try:
	result = subprocess.check_output(["sudo lsof -i:5000 -t"], shell=True)

	process = result.decode('ascii')

	process = process.split("\n")
except Exception as e:
	# exit()
	pass


if('process' in globals()):
	for i in range(len(process)):
		if(process[i] != ""):
			try:
				my_str = "kill " + str(process[i])
				print(my_str)
				os.system(my_str)	  # you can use subprocess as well
				print(str(process[i]) + " is killed")
			except Exception as e:
				print(e)
