#***************************************************************************
#**************** OFFENSIVE SECURITY WITH KALI LINUX ***********************
#***************************************************************************

# KALI MENU
updatedb			# builds a FileSystem's database
locate sbd.exe			# locates files in db
which sbd			# searches through $PATH-defined directories
find / -name sbd*		# searches recursively in any given path (most aggressive)

# KALI MANAGE
passwd				# Changes default kali password
service ssh start 		# Starting the SSH service
netstat -antp | grep sshd		# searches output for ssh
