# This is a simple Python script to check which external IP address you have. First we are importing the urllib and re modules.
import urllib
import re

print("We will try to open this url, in order to get IP Address.")

url = "http://checkip.dyndns.org"

print(url)

request = urllib.urlopen(url).read()

theIP = re.findall(r"d{1,3}.d{1,3}.d{1,3}.d{1,3}", request)

print("your IP Address is: ", theIP)
