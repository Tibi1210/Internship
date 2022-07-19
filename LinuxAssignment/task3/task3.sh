#!/bin/bash

host=`head -n 1 config.cfg`
database=`head -n 2 config.cfg | tail -n 1`
username=`head -n 3 config.cfg | tail -n 1`
passwd=`head -n 4 config.cfg | tail -n 1`
workingdir=`head -n 5 config.cfg | tail -n 1`
query=`head -n 6 config.cfg | tail -n 1`


cd ~
mkdir $workingdir
cd $workingdir

psql -c "$query" > test.csv

