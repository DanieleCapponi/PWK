#!/bin/bash

# save my IP on subnet
ifconfig eth0 | grep "inet" | grep "netmask" | cut -d " " -f 10 > mioip
p="."				# point char

# save my ip to update in loop
IP="$(cat mioip | cut -d '.' -f 1)"$p"$(cat mioip | cut -d '.' -f 2)"$p"$(cat mioip | cut -d '.' -f 3)$p"

# create temp file
echo "" > temp
echo starting IP sweep over subnet "("$IP"0/24)..."

# ping every host in my network and save result in temp
for val in {1..254}; do ((ping -c 10 -i 0.1 $IP$val &) >> temp) >> temp; done

echo 

# save hosts up in IPs_up.txt
grep "from " temp | cut -d " " -f 4 | cut -d ":" -f 1 | sort -u > IPs_up

echo "***************" $(wc IPs_up | cut -d " " -f 3) HOSTS ARE RESPONSIVE "***************"

cat IPs_up
echo

# remove temp files
rm IPs_up
rm temp
rm mioip
