import urllib2
import urllib
import re
from os.path import expanduser
import os
from bs4 import BeautifulSoup
import json
import webbrowser

base='http://www.iplocationfinder.com/'
ip_addr = raw_input()
website=urllib2.urlopen(base+ip_addr)
html=website.read()
soup = BeautifulSoup(html,'html.parser')
for child in soup.find_all("th"):
	if 'Latitude:' in child.contents[0]:
		lat = child.next_sibling.string
	if 'Longitude:' in child.contents[0]:
		lon = child.next_sibling.string
query_string = 'http://maps.google.com/maps?q=loc:'+lat+','+lon+'&z=17'
new = 2
webbrowser.open(query_string,new=new)

