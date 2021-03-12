#!/bin/python

import sys,os
import socket
from sys import platform
from datetime import datetime

count=0
if platform == "linux" or platform == "linux2":
	os.system("figlet PORT SCANNER")
try:
	target=socket.gethostbyname(sys.argv[1])
	try:
		startPort=int(sys.argv[2])
		endPort=int(sys.argv[3])
		print(f"Scanning from port {startPort} to {endPort}")
	except:
		print("Since starting and ending ports are not given, default sanning ports are 1 to 1000")
		startPort=1
		endPort=1000
except:
	print("Invalid Amount of Argument.")
	print("Syntax: python3 scanner.py <ip> <startingPort> <endingPort>")
	sys.exit()
	
print("-"* 50)
print("Starting V35HR4J's Port Scanner")
print("scanning target "+target)
print("Time Started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(startPort,endPort):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result=s.connect_ex((target,port)) 
		if result == 0:
			count+=1
			print("port {} is open.".format(port))
	if count==0:
		print("None Open Ports found")
		s.close()
except KeyboardInterrupt:
	print("\n Exiting Program")
	sys.exit()
except socket.gaierror:
	print("Host name could not be resolved")
	sys.exit()
except socket.error:
	print("Couldn't connect to the server")
	sys.exit()
