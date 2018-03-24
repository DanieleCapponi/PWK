#!/bin/bash

site=$1
rm index.*

wget "$site"
grep "href=" index.html | cut -d "/" -f 3 | grep "\." | cut -d '"' -f 1 | sort -u > list
echo "***** Host discovered: *****"
echo
cat list
echo
for url in $(cat list); do host $url; done | grep "has address " | cut -d " " -f 4 | sort -u

rm list
