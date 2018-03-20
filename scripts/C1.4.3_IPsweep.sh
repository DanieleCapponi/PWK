#!/bin/bash

IP="192.168.0."

echo "" > temp

echo starting IP sweep over subnet...
echo

for val in {1..254}; do ((ping -c 10 -i 0.1 $IP$val &) >> temp) >> temp; done
 
echo ---\> IPs_up.txt
echo 
	
grep "from " temp | cut -d " " -f 4 | cut -d ":" -f 1 | sort -u > IPs_up.txt

echo "***************" $(wc IPs_up.txt | cut -d " " -f 2) HOSTS UP "***************"

cat IPs_up.txt
echo
rm temp
