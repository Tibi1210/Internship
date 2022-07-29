#!/bin/bash

host='localhost'
database='azure'
username='student'
passwd='admin'

export PGPASSWORD=$passwd

#psql -h $host -U $username -c "DROP DATABASE $database"

psql -h $host -U $username -c "CREATE DATABASE $database"

psql -h $host -d $database -U $username -f ddl.sql

python3 - <<END
import api
api.generate_all(100)
END

rm -r __pycache__