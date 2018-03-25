#!/usr/bin/python

import threading
import time
import socket

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
		ip = '192.168.0.'+str(self.counter)
		port = 25
		timeout = 3
		
		ports = {'tcpM':1, 'udp':7, 'ftpD':20, 'ftpC':21, 'ssh':22, 'tlnt':23, 'smtp':25, 'dns':53,
		'dhcpS':67, 'dhcpC':68, 'http':80, 'kerb':88, 'pop3':110, 'imap4':143, 'https':443,
		'smtp':465, 'syslog':514, 'smtp':587, 'imap4S':993, 'pop3S':995}
		
		for el in ports :
			try:
				socket.create_connection((ip, el), timeout)
				print "[*]Connected :\t" + ip + ": " + str(ports[el]) + " (" + el + ")"
				output(ip, "[*]Connected :\t" + ip + ":" + el, el)
				self.flag = 0
			except Exception, arg:
				if (str(arg).find("refused", 0) > -1) :
					if self.flag == 1:
						print "[*]Host UP :\t" + ip
					self.flag = 0
			
			
	def output(ip, s, el):
		if self.result.find(ip) > -1 :
			self.result += "\t\t\t open port: " + el + "(" + str(el) + ")"
		else :
			self.result += "\n[*] IP: " + ip
			
		
		
					
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
	
