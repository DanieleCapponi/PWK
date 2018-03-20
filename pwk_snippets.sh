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

grep "href=" index.html | cut -d "/" -f 3 | grep "\." | cut -d '"' -f 1 | sort -u
