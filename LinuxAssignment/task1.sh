#!/bin/bash

cd ~
mkdir test
cd test
touch etc_log.txt
chmod 666 etc_log.txt
ls -l /etc | tail -n +2 | awk '{print $9 " " $1 " " $5 " " $6 " " $7}' > etc_log.txt
ls -l /run | tail -n +2 | awk '{print $9 " " $1 " " $5 " " $6 " " $7}' > run_log.txt
cat etc_log.txt run_log.txt | tee unsorted.txt | sort -r > reversed.txt 
