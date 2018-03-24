import sys
import os

ips = "192.168.254."

i = 1
response, listed = "", ""
os.system("echo '' > pingSweep.txt")

while (i < 255):
	response = (os.system("ping -c 2 -i 0.1 -q " + ips + str(i) + " >> pingSweep.txt"))
	i = i+1
	listed += " " + str(response)
	print(response)
	#if response.find("from"):
	#	listed += ips + str(i)

print (listed)
