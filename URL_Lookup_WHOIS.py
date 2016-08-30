#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
import cgi
from ipwhois import IPWhois
from pprint import pprint


cgitb.enable()

print "Content-Type: text/plain;charset=utf-8"
print
form = cgi.FieldStorage()
URL = form["Field"].value
obj = IPWhois(URL)
response = obj.lookup_rdap(depth=1)
pprint(response)
# print "Hello World!"

