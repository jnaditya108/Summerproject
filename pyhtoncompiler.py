#!/usr/bin/python3


import cgi
import cgitb
cgitb.enable()

print("Content-type: text/html")
print()

# HTML header
print("<html>")
print("<head><title>Python Compiler</title></head>")
print("<body>")

# Get user's Python code from the form
form = cgi.FieldStorage()
user_code = form.getvalue("code")

# Execute the user's code
try:
    exec(user_code)
except Exception as e:
    print("Error:", e)

# HTML footer
print("</body>")
print("</html>")
