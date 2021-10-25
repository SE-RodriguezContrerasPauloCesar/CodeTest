from django.http import HttpResponse
from requests import get
import socket 
import re
from collections import Counter

def index(request):    
    print("This is a codetest")

"""This function will be called by the web service every time it handles a request

    Parameters
    ----------
    ip_address : str
        string containing an IP address
"""
def request_handled(ip_address):         
    IPAddr = socket.gethostbyname(ip_address)    
    print("The Computer IP Address is:" + IPAddr) 

""" This function returns the top 100 IP addresses by request count, with the highest traffic IP address first
"""
def top100():    
    cnt = Counter()
    ipre = re.compile(r'^(?P<ip>(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])) - -')
    with open(infilename) as infile:
        for line in infile:
            m = ipre.match(line)
            if m is not None:
                ip = m.groupdict()['ip']
                cnt[ip] += 1

""" It's used to forget about all IP addresses and tallies.
"""
def clear():
# Making a DELETE request
r = requests.delete('list_of_ips', data ={'key':'value'})
  
# check status code for response received
# success code - 200
print(r)
  
# print content of request
print(r.json())
