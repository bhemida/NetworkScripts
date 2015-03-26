#!/usr/bin/python

#This Python Script Written By @b4s3mh3lmy - #OSCP OS-11235
#This Script search for shellcodes
#Source Of This Shell Codes is Shell Storm http:///www.shell-storm.org/
#Use it ./ShellCodes.py windows*local - ./Shellcodes.py word1*word2*word3

import sys
import urllib2
import re

Burl = "http://www.shell-storm.org/api/?s="
Bsearch = sys.argv[1]

Breq = urllib2.Request(Burl+Bsearch)
Bres = urllib2.urlopen(Breq)

#Parsing The Output
Bresult = []
Bdump = Bres.read().split("\n")
for Brecord in Bdump:
	Bresult.append(Brecord.replace("::::", " - "))

for Bfinding in Bresult[:-1]:
	print "[*]" + (Bfinding) 
