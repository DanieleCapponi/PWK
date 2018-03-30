#!/usr/bin/python

import os
import threading
import time
import sys
import socket
import os.path

class SweepTh (threading.Thread):
	
	result = ""
	flag = 1
	
	def __init__(self, threadID, name, ip):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.ip = ip
			
	def run(self):
		port = 25
		timeout = 3
		fName = "temp.ip."+ self.ip[self.ip.rfind(".")+1 : len(self.ip)]
		
		ports = {'tcpM':1, 'tcpCMU':2, 'tcpCCP':3, 'udp':7, 'BifUDP':8, 'dayTime':13, 'ftpD':20, 'ftpC':21, 'ssh':22, 'tlnt':23, 'smtp':25, 'dns':53,
		'dhcpS':67, 'dhcpC':68, 'http':80, 'kerb':88, 'pop3':110, 'imap4':143, 'https':443, 'smtp':465, 'syslog':514, 'smtp':587, 'imap4S':993, 
		'pop3S':995, 'socks':1080, 'openVPN':1194, 'msSQL':1433, 'msSQLm':1434, 'bigbrother':1984, 'networkFS':2049, 'mySQL':3306, 'rdp':3389,
		'subversion':3690, 'sip':5060}
		
		file = open(fName, "w")
		file.write("[*]"+self.ip+":")
		
		for el in ports :
			try:
				socket.create_connection((self.ip, el), timeout)
				file.write("\n      CONNECTION port:\t" + str(ports[el]) + " (" + el + ")")
				self.flag = 0
			except Exception, arg:
				if (str(arg).find("refused", 0) > -1) :
					if self.flag == 1:
						file.write("\tHost is UP")
					self.flag = 0
		
		file.close()
		file = open(fName, "r")
		tempStr = file.read()
				
		if ("Host" not in tempStr) and ("CONNECTION" not in tempStr):
				os.remove(fName)
		else:
			file.close()
			print("[*] Host:\t" + self.ip + "\tis responsive...")
		
