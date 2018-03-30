#!/usr/bin/python

import os
import threading
import time
import sys
import socket
import os.path
from SweepTh import SweepTh



def verifyIP(ip) :
	
	if "/" not in ip or "." not in ip  or ip == "" :
		return False

	i1 = int(ip[0 : ip.find(".")])
	ip = ip[ip.find(".")+1 : len(ip)]
	i2 = int(ip[0 : ip.find(".")])
	ip = ip[ip.find(".")+1 : len(ip)]
	i3 = int(ip[0 : ip.find(".")])
	ip = ip[ip.find(".")+1 : len(ip)]
	i4 = int(ip[0 : ip.find("/")])
	cidr = int(ip[ip.find("/")+1 : len(ip)])
	
	if i1 < 0 or i1 > 255 or i2 < 0 or i2 > 255 or i3 < 0 or i3 > 255 or i4 < 0 or i4 > 254 or cidr < 2 or cidr > 31:
		return False


try:
	try:
		ip = sys.argv[1]			# take ip arg from user
	except Exception:
		print "*** You need to specify a network ip addres (x.x.x.x/cidr)"
		sys.exit(1)
		
	if verifyIP(ip) is False :
		raise Exception("*** Malfomed ip address (x.x.x.x/cidr) ")
except Exception as e :
	print e
	sys.exit(2)

print ("\t -- Starting IP-Sweep over subnet " + ip + " --")

			
threadLock = threading.Lock()
threads = []		

ip = ip[0 : ip.rfind(".")+1]


i = 1
while (i < 255):
	thread = SweepTh(i, "Thread_0."+str(i), ip+str(i))
	thread.start()
	threads.append(thread)
	i = i+1
	
	
for th in threads:
	th.join()
	
res = ""
i = 1
hmh = 0						# How may hosts are up
while (i < 255):
	if os.path.isfile('./temp.ip.'+str(i)):
		f = open('./temp.ip.'+str(i))
		res += "\n" + f.read() + "\n"
		f.close()
		os.remove("./temp.ip."+str(i))
		hmh = hmh+1
	i = i+1

	
file = open("./Hosts.txt", "w+")
file.write(res)
file.close()

print "\n[***] " + str(hmh) + " Hosts are up on subnet " + ip + "0/24"
print "[***] File 'Host.txt' created"
	

