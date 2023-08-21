#!/usr/bin/python3

print("content-type: text/html")

print()

import subprocess

s=subprocess.getoutput("sudo docker ps -a")

leng=len(s.split("\n"))-1
for i in range(1,leng):
    al=s.split("\n")
    ls=al[1:]
    lss=ls[0].split()

    finalimage=lss[0]+":"+lss[1]

    print(finalimage)
    print("\n")
