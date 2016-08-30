#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import cgi
import re

"""
CGI flag for debugging purpose
True = execute python through html
False = execute python directly
"""
CGI = True
MalwareURL = False

"""
Regex to Match URL in various format
This would match cases like:
www.google.com
https://www.google.com
http://net.tutsplus.com/about
Detail: http://code.tutsplus.com/tutorials/8-regular-expressions-you-should-know--net-6149
"""
regex = r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'

cgitb.enable()
print "Content-Type: text/plain;charset=utf-8"
print
form = cgi.FieldStorage()

if CGI:
    URL = form["Field"].value
else:
    URL = "bolo100.com"

# Grep the domain from input URL to match against db
match = re.search(regex, URL)
Domain = "{0}.{1}".format(match.group(2), match.group(3))

# Connect db and search the domain is in list of malwares
with open("simple_malware.txt") as f:
    for line in f:
        if re.search(Domain, line):
            MalwareURL = True
            break

# Response format
# TODO: Change response as a JSON {validated: "True"/"False"} 
if MalwareURL:
    print "This URL is Malware (Not safe)"
else:
    print "This URL is Safe"
