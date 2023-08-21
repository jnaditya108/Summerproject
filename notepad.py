#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi

data=cgi.FieldStorage()

mydaat=data.getalue("w")

file_path = "usr/bin/data.txt"  


with open(file_path, "w") as file:
    file.write(data)

print("Note Saved Successfully !!")
