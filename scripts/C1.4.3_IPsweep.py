#!/usr/bin/python

import threading
import time
import socket

class myThread (threading.Thread):
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
				print "[*]Connected :\t" + ip + ":" + el
			except Exception, arg:
				if (str(arg).find("refused", 0) > -1) :
					print "[*]Host UP :\t" + ip + ":" + el
					
					
						
i = 1
while (i < 255):
	thread = myThread(i, "Thread_0."+str(i), i)
	thread.start()
	i = i+1
