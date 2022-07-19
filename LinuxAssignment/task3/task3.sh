#!/bin/bash

host=`head -n 1 config.cfg | awk '{print $2}'`
database=`head -n 2 config.cfg | tail -n 1 | awk '{print $2}'`
username=`head -n 3 config.cfg | tail -n 1 | awk '{print $2}'`
passwd=`head -n 4 config.cfg | tail -n 1 | awk '{print $2}'`
workingdir=`head -n 5 config.cfg | tail -n 1`
query=`head -n 6 config.cfg | tail -n 1`
year=`head -n 7 config.cfg | tail -n 1 | awk '{print $1}'`
columns=`head -n 7 config.cfg | tail -n 1 | awk '{print $2}'`
order=`head -n 7 config.cfg | tail -n 1 | awk '{print $3}'`




mkdir $workingdir
cd $workingdir

echo $columns > test_$year.txt
psql -c "$query" | tail -n +3 | head -n -2 >> test_$year.txt

gzip test_$year.txt
