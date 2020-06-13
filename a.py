# coding: UTF-8
import requests
from bs4 import BeautifulSoup

URL = 'https://www.google.com/search?q=%E7%8C%AB&tbm=isch&rlz=1C5CHFA_enJP897JP897&hl=ja&ved=2ahUKEwi4hPfn4-7pAhUF7JQKHTyfAUAQBXoFCAEQyAE&biw=1440&bih=789'

soup = BeautifulSoup(requests.get(URL).content, 'lxml')

srcs = []
for link in soup.find_all('img'):
    
    if link.get('src').find('.jpg'):
        srcs.append(link.get('src'))
        
    elif link.get('src').find('.png'):
        srcs.append(link.get('src'))
        
    elif link.get('src').find('.jpeg'):
        srcs.append(link.get('src'))



open('/img').write(srcs.content)

print(ok)