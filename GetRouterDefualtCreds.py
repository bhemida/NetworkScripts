#!/usr/bin/python
'''
This Script Writen By @bh3lmy
'''
import urllib,urllib2
import sys
from bs4 import BeautifulSoup

if len(sys.argv) >2 or len(sys.argv)<2:
	print '''[*]This Script Writen By @bh3lmy
[*]Use This Script as #ScriptName.py RouterName'''
	sys.exit(0)


base_url = "https://routerpasswords.com/router-password/?router="
Device = sys.argv[1].upper()

print "[*]Looking For %s Defualt username and Passwords ... "%Device

url = base_url+Device

request = urllib2.Request(url)
response = urllib2.urlopen(request)

soup = BeautifulSoup(response, features="html.parser")

print "[*]Finding are Below :"
print "[*]Model\tProtocol\tUserName\tPassword"
for i in soup.find_all('tr'):
	for y in i.find_all('td'):
		if y.string == "%s"%Device:
			print "\n[*]",
		else:
			print str(y.text)+"\t",
print "\n"
