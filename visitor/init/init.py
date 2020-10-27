from bezmouse import *
import pyautogui
import time
from os import path
import random
import importlib.machinery
import json
import requests
import re


username = os.getenv('USERNAME')

visitor_lib = importlib.machinery.SourceFileLoader('visitor_lib', 'visitor_lib/visitor_lib.py').load_module()

def scramble(string):
	l = list(string)
	random.shuffle(l)
	return ''.join(l)

def get_password():
	s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	s1 = "0123456789"
	s2 = "!@#$%^&*()?"
	p =  "".join(random.sample(s,5))
	p2 =  "".join(random.sample(s1,4))
	p3 =  "".join(random.sample(s2,5))
	return scramble(p+p2+p3)

def get_username():
	s = "abcdefghijklmnopqrstuvwxyz"
	s1 = "0123456789"
	s2 = "!@#$%^&*()?"
	p =  "".join(random.sample(s,8))
	p2 =  "".join(random.sample(s1,2))
	return sp+p2

def get_name():
	s = "abcdefghijklmnopqrstuvwxyz"
	s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	p =  "".join(random.sample(s,random.randint(4,8)))
	p2 =  "".join(random.sample(s1,1))
	return p2+p

def init():

	time.sleep(random.randint(25000, 26000)/1000)
	visitor_lib.move_to_area_relative("visitor_lib/mp.png", 41, 51, 17, 16, True, crt=0.65)
	time.sleep(random.randint(2000, 3000)/1000)

	#install buster addon
	visitor_lib.browser_open_url('https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl')
	time.sleep(random.randint(15000, 16000)/1000)
	visitor_lib.move_to_area_relative("init/atc.png", 23, 18, 118, 24, True)
	time.sleep(random.randint(12000, 13000)/1000)
	visitor_lib.move_to_area_relative("init/cancel.png", 105, 15, 114, 18, True, crt=0.8)
	time.sleep(random.randint(10000, 11000)/1000)


	if path.exists('../init.txt'):
		with open('../init.txt', 'r') as infile:
			init = json.load(infile)

	if path.exists('../ip.txt'):
		with open('../ip.txt', 'r') as infile:
			ip = infile.read()

	tries = 3

	try:
		resp = requests.get(init['supervisor_url']+"/update?name="+username+"&ip="+ip)
	except:
		pass

	fn = get_name()
	ln = get_name()
	un = get_username()
	pw = get_password()
	em = un+"@protonmail.com"

	rep = 0
	try:
		resp = requests.get(init['supervisor_url']+"/reproduce")
		if resp.json()['reproduce'] == "reproduce":
			rep = 1
	except:
		pass

	if rep:
		#protonmail
		protonmail = 0
		for y in range(0, tries):
			visitor_lib.browser_open_url('https://protonmail.com/signup')
			time.sleep(random.randint(15000, 16000)/1000)
			visitor_lib.move_to_area_relative("init/free.png", 695, 11, 187, 28, True)
			pyautogui.scroll(-7)
			time.sleep(random.randint(3000, 4000)/1000)
			visitor_lib.move_to_area_relative("init/free.png", 722, 322, 192, 30, True)
			time.sleep(random.randint(18000, 20000)/1000)
			visitor_lib.move_to_area_relative("init/one.png", 88, 86, 78, 7, True)
			pyautogui.write(un, interval = 0.1)
			pyautogui.press('tab')
			pyautogui.press('tab')
			pyautogui.write(pw, interval = 0.1)
			pyautogui.press('tab')
			pyautogui.press('tab')
			pyautogui.write(pw, interval = 0.1)
			pyautogui.scroll(-7)
			time.sleep(random.randint(3000, 4000)/1000)
			visitor_lib.move_to_area_relative("init/create_acc.png", 13, 15, 176, 38, True)
			time.sleep(random.randint(3000, 4000)/1000)
			uau = visitor_lib.move_to_area_relative("init/confirm.png", 21, 19, 68, 25, True)
			if uau != 'success':
				visitor_lib.browser_open_url('https://protonmail.com/login')
				time.sleep(random.randint(15000, 16000)/1000)
				visitor_lib.move_to_area_relative("init/pmail.png", -72, 127, 87, 21, True)
				pyautogui.write(em, interval = 0.1)
				pyautogui.press('tab')
				pyautogui.write(pw, interval = 0.1)
				pyautogui.press('tab')
				pyautogui.press('tab')
				pyautogui.press('enter')
				time.sleep(random.randint(18000, 20000)/1000)
				protonmail = 1
				break
			else:
				time.sleep(random.randint(3000, 4000)/1000)
				cpt = visitor_lib.move_to_area_relative("init/imnotarobot.png", -20, -20, 10, 10, False)
				time.sleep(random.randint(3000, 4000)/1000)
				if cpt == "success":
					visitor_lib.solve_captcha_buster(scroll=-10)
					time.sleep(random.randint(1000, 2000)/1000)
				else:
					visitor_lib.move_to_area_relative("init/email.png", 13, 12, 9, 11, True)
					time.sleep(random.randint(1000, 2000)/1000)
					pyautogui.hotkey('ctrl', 'n')
					visitor_lib.browser_open_url('https://tempmail.ninja/')
					time.sleep(random.randint(15000, 16000)/1000)
					visitor_lib.move_to_area_relative("visitor_lib/home_chrome.png", -8, 92, 205, 152, True)
					pyautogui.scroll(-6)
					time.sleep(random.randint(3000, 4000)/1000)
					visitor_lib.move_to_area_relative("init/create_temp.png", 29, 18, 81, 5, True)
					time.sleep(random.randint(3000, 4000)/1000)
					pyautogui.press("f11")
					time.sleep(random.randint(3000, 4000)/1000)
					pyautogui.press("f11")
					time.sleep(random.randint(1000, 2000)/1000)
					visitor_lib.move_to_area_relative("init/ctce.png", 127, -165, 120, 24, True)
					time.sleep(random.randint(1000, 2000)/1000)
					visitor_lib.move_to_area_relative("init/ctce.png", 126, -127, 147, 139, True)
					time.sleep(random.randint(1000, 2000)/1000)
					visitor_lib.move_to_area_relative("init/ctce.png", 7, 9, 86, 21, True)
					time.sleep(random.randint(4000, 5000)/1000)
					pyautogui.scroll(6)
					time.sleep(random.randint(3000, 4000)/1000)
					visitor_lib.move_to_area_relative("init/copy_tempmail.png", 11, 28, 24, 22, True)
					time.sleep(random.randint(1000, 2000)/1000)
					pyautogui.hotkey('ctrl', 'w')
					time.sleep(random.randint(1000, 2000)/1000)
					visitor_lib.move_to_area_relative("init/five.png", 84, 271, 92, 16, True)
					pyautogui.hotkey('ctrl', 'v')
					visitor_lib.move_to_area_relative("init/five.png", 324, 269, 42, 24, True)
					time.sleep(random.randint(4000, 5000)/1000)
					pyautogui.hotkey('ctrl', 'n')
					visitor_lib.browser_open_url('https://tempmail.ninja/')
					time.sleep(random.randint(20000, 21000)/1000)
					visitor_lib.move_to_area_relative("init/verification_open.png", 11, 19, 34, 18, True)
					time.sleep(random.randint(3000, 4000)/1000)
					visitor_lib.move_to_area_relative("init/proton_ver.png", 47, 287, 40, 10, True)
					pyautogui.click()
					pyautogui.click()
					pyautogui.hotkey('ctrl', 'c')
					time.sleep(random.randint(1000, 2000)/1000)
					pyautogui.hotkey('ctrl', 'w')
					time.sleep(random.randint(3000, 4000)/1000)
					pyautogui.press("f11")
					time.sleep(random.randint(3000, 4000)/1000)
					pyautogui.press("f11")
					visitor_lib.move_to_area_relative("init/five.png", 89, 352, 100, 12, True)
					pyautogui.hotkey('ctrl', 'v')
					pyautogui.scroll(-7)
					time.sleep(random.randint(3000, 4000)/1000)
					visitor_lib.move_to_area_relative("init/create_acc.png", 13, 15, 176, 38, True)
					time.sleep(random.randint(3000, 4000)/1000)
					visitor_lib.move_to_area_relative("init/confirm.png", 21, 19, 68, 25, True)
					time.sleep(random.randint(10000, 12000)/1000)
						

				visitor_lib.move_to_area_relative("init/complete.png", 13, 17, 201, 40, True)
				time.sleep(random.randint(25000, 26000)/1000)
				pms = visitor_lib.move_to_area_relative("init/success.png", 386, 202, 44, 21, True)
				if pms == 'success':
					protonmail = 1
					break


		#heroku
		if protonmail:
			for x in range(0, tries):
				visitor_lib.browser_open_url('https://signup.heroku.com/')
				time.sleep(random.randint(8000, 10000)/1000)
				visitor_lib.move_to_area_relative("init/fracc.png", 434, 27, 278, 19, True)
				pyautogui.write(fn, interval = 0.1)
				pyautogui.press('tab')
				pyautogui.write(ln, interval = 0.1)
				pyautogui.press('tab')
				pyautogui.write(em, interval = 0.1)
				pyautogui.scroll(-10)
				time.sleep(random.randint(4000, 5000)/1000)
				visitor_lib.move_to_area_relative("init/dn.png", 428, -36, 280, 35, True)
				pyautogui.press('down')
				pyautogui.press('down')
				pyautogui.press('enter')
				time.sleep(random.randint(1000, 2000)/1000)
				visitor_lib.move_to_area_relative("init/dn.png", 429, 133, 286, 32, True)
				pyautogui.press('down')
				pyautogui.press('down')
				pyautogui.press('down')
				pyautogui.press('enter')
				time.sleep(random.randint(1000, 2000)/1000)
				cpt = visitor_lib.solve_captcha_buster()
				time.sleep(random.randint(1000, 2000)/1000)
				if cpt:
					time.sleep(random.randint(6000, 7000)/1000)
					visitor_lib.move_to_area_relative("init/cfa.png", 16, 17, 286, 34, True)
					time.sleep(random.randint(8000, 10000)/1000)

					for x in range(0, 6):
						visitor_lib.browser_open_url('https://mail.protonmail.com/inbox')
						time.sleep(random.randint(10000, 11000)/1000)
					visitor_lib.move_to_area_relative("init/pml.png", 217, 115, 75, 38, True)
					time.sleep(random.randint(4000, 5000)/1000)
					visitor_lib.move_to_area_relative("init/load.png", 12, 11, 47, 22, True)
					time.sleep(random.randint(1000, 2000)/1000)
					pyautogui.scroll(-3)
					time.sleep(random.randint(3000, 4000)/1000)
					visitor_lib.move_to_area_relative("init/hl.png", 17, 10, 83, 40, True)
					for x in range(0,13):
						pyautogui.press('tab')
						time.sleep(0.1)
					pyautogui.press('enter')
					time.sleep(random.randint(6000, 7000)/1000)
					visitor_lib.move_to_area_relative("init/lc2.png", 58, 73, 136, 14, True)
					pyautogui.click()
					pyautogui.click()
					pyautogui.hotkey('ctrl', 'c')
					visitor_lib.move_to_area_relative("visitor_lib/home_chrome.png", 9, 11, 15, 15, True)
					time.sleep(2)
					visitor_lib.move_to_area_relative("visitor_lib/home_chrome.png", 111, 8, 59, 13, True)
					for x in range(0, 50):
						pyautogui.press('backspace')
					pyautogui.hotkey('ctrl', 'v')
					pyautogui.press('enter')
					time.sleep(random.randint(16000, 18000)/1000)
					visitor_lib.move_to_area_relative("init/sp.png", -48, 210, 96, 21, True)
					pyautogui.write(pw, interval = 0.1)
					pyautogui.press('tab')
					pyautogui.write(pw, interval = 0.1)
					pyautogui.scroll(-4)
					time.sleep(random.randint(3000, 4000)/1000)
					visitor_lib.move_to_area_relative("init/spli.png", 25, 37, 374, 30, True)
					time.sleep(random.randint(8000, 9000)/1000)
					visitor_lib.move_to_area_relative("init/proceed.png", 33, 224, 237, 27, True)
					time.sleep(random.randint(35000, 36000)/1000)
					visitor_lib.move_to_area_relative("visitor_lib/home_chrome.png", -8, 92, 205, 152, False)
					pyautogui.scroll(-20)
					move_to_area(504, 642, 36, 10, 20, random.randint(4, 12))
					pyautogui.mouseDown()
					time.sleep(random.randint(20, 100)/1000)
					pyautogui.mouseUp()
					move_to_area(504, 642, 36, 10, 20, random.randint(4, 12))
					pyautogui.mouseDown()
					time.sleep(random.randint(20, 100)/1000)
					pyautogui.mouseUp()
					time.sleep(random.randint(15000, 16000)/1000)
					hs = visitor_lib.move_to_area_relative("init/hm.png", -207, 11, 102, 24, False)
					if hs != "success":
						visitor_lib.browser_open_url('https://id.heroku.com/login')
						time.sleep(random.randint(20000, 21000)/1000)
						pyautogui.write(em, interval = 0.1)
						pyautogui.press('tab')
						pyautogui.write(pw, interval = 0.1)
						pyautogui.press('tab')
						pyautogui.press('enter')
						time.sleep(random.randint(20000, 21000)/1000)
						hs = visitor_lib.move_to_area_relative("init/hm.png", -207, 11, 102, 24, False)
					if hs == "success":
						visitor_lib.browser_open_url(init['deploy_url'])
						time.sleep(random.randint(8000, 9000)/1000)
						visitor_lib.move_to_area_relative("init/gl.png", 9, 155, 104, 17, True)
						time.sleep(random.randint(1000, 2000)/1000)
						pyautogui.write(un, interval = 0.1)
						pyautogui.press('tab')
						pyautogui.press('tab')
						pyautogui.write(fn, interval = 0.1)
						pyautogui.press('tab')
						pyautogui.write(ln, interval = 0.1)
						pyautogui.press('tab')
						pyautogui.write(pw, interval = 0.1)
						pyautogui.press('tab')
						pyautogui.press('tab')
						pyautogui.press('tab')
						pyautogui.write(un, interval = 0.1)
						pyautogui.press('tab')
						pyautogui.scroll(-8)
						time.sleep(random.randint(3000, 4000)/1000)
						try:
							resp = requests.get(init['supervisor_url']+"/reproduce")
							if resp.json()['reproduce'] == "reproduce":
								visitor_lib.move_to_area_relative("init/da.png", 10, 16, 90, 22, True)
						except:
							pass
						break

