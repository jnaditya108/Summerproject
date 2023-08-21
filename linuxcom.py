#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi 
import subprocess

data=cgi.FieldStorage()

daat1=data.getvalue("na")

sub=subprocess.getoutput(daat1)

print(sub)
