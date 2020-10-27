import requests
from os import path
import os
import json
import time

if path.exists('init.txt'):
	with open('init.txt', 'r') as infile:
		init = json.load(infile)

username = os.getenv('USERNAME')

if path.exists('../ip.txt'):
	with open('../ip.txt', 'r') as infile:
		ip = infile.read()

while True:
	try:
		resp = requests.get(init['supervisor_url']+"/update?name="+username+"&ip="+ip)
	except:
		pass
	time.sleep(60*60)

	