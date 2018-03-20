#***************************************************************************
#**************** OFFENSIVE SECURITY WITH KALI LINUX ***********************
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


