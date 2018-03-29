#!/usr/bin/python

import os
import threading
import time
import sys
import socket
import os.path

global result

class myThread (threading.Thread):
	
	result = ""
	flag = 1
	
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
			
	def run(self):
		ip = '192.168.254.'+str(self.counter)
		port = 25
		timeout = 3
		fName = "temp.ip."+str(self.counter)
		
		file = open(fName, "w")
		file.write("[*]"+ip+":")
		
		p = 1
		while p < 65536 :
			try:
				socket.create_connection((ip, p), timeout)
				file.write("\n      CONNECTION port:\t" + str(p))
				self.flag = 0
			except Exception, arg:
				if (str(arg).find("refused", 0) > -1) :
					if self.flag == 1:
						file.write("\n      Host is UP")
					self.flag = 0
		
		file.close()
		file = open(fName, "r")
		tempStr = file.read()
				
		if ("Host" not in tempStr) and ("CONNECTION" not in tempStr):
				os.remove(fName)
		else:
			file.close()
			print("[*]Host:\t" + ip + "\tis responsive...")
		
			
		
print ("\t -- Starting IP-Sweep over subnet --")
					
threadLock = threading.Lock()
threads = []				
			
i = 1
while (i < 255):
	thread = myThread(i, "Thread_0."+str(i), i)
	thread.start()
	threads.append(thread)
	i = i+1
	
	
for th in threads:
	th.join()
	
res = ""
i = 1
while (i < 255):
	if os.path.isfile('./temp.ip.'+str(i)):
		f = open('./temp.ip.'+str(i))
		res += "\n" + f.read() + "\n"
		f.close()
		os.remove("./temp.ip."+str(i))
	i = i+1

	
file = open("./Hosts.txt", "w+")
file.write(res)
file.close()
	
print "[***] File 'Host.txt' created"
	
	
