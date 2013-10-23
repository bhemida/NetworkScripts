#!/usr/bin/python
'''
This Script Writen By @b4s3mh3lmy 
'''
import urllib,urllib2
import sys
from bs4 import BeautifulSoup

if len(sys.argv) >2 or len(sys.argv)<2:
	print '''[*]Please Use This Script in Ethical Hacking or Educational purpose
[*]Error: Too many inputs
[*]Use This Script Like That #ScriptName.py RouterName'''
	sys.exit(0)


url = "http://routerpasswords.com"
Device = sys.argv[1].upper()

print "[*]Looking For %s Defualt username and Passwords ... "%Device

args = {'findpass':'1','router':'%s'%Device,'findpassword':'Find Password'}
decode_args = urllib.urlencode(args)

request = urllib2.Request(url,decode_args)
response = urllib2.urlopen(request)

soup = BeautifulSoup(response)

print "[*]Finding are Below :"
print "[*]Model\tProtocol\tUserName\tPassword"
for i in soup.find_all('tr'):
	for y in i.find_all('td'):
		if y.string == "%s"%Device:
			print "\n[*]",
		else:
			print "\""+str(y.text)+"\""+" ",
print "\n"
