#!/usr/bin/python

'''
This Script Writen By @b4s3mh3lmy 
'''

import urllib
import sys
import re
from bs4 import BeautifulSoup
from termcolor import colored

PORT = sys.argv[1]

if len(sys.argv) >2 or len(sys.argv)<2:
	print '''[*]Please Use This Script in Ethical Hacking or Educational purpose
[*]Error: Too many inputs
[*]Use This Script Like That #ScriptName.py PortNumber'''
	sys.exit(0)

url_base = "http://www.pc-library.com/ports/tcp-udp-port/%s/"%PORT
print "[*] Searching For Port %s\n" %PORT
Submit = urllib.urlopen(url_base)
soup = BeautifulSoup(Submit)
for x in soup.find_all('div', id=re.compile('^desc*')):
	print "[*] "+x.string
print ""
