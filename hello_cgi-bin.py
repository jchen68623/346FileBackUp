#!/usr/bin/python3

import cgi, cgitb

form = cgi.FieldStorage()

first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

print ("Content-type: text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello World - Second CGI Program</title>')
print ('</head>')
print ('<body>')
print ('<h2>Hello World! {} {} </h2>' .format(first_name, last_name))
print ('</body>')
print ('</html>')

