import requests
import random
import shutil
import bs4
import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context
def image(data):
    Res = requests.get("https://www.google.com/search?hl=jp&q=" + data + "&btnG=Google+Search&tbs=0&safe=off&tbm=isch")
    Html = Res.text
    Soup = bs4.BeautifulSoup(Html,'lxml')
    links = Soup.find_all("img")
    link = random.choice(links).get("src")
    return link
def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name+".png", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
def code():
    code = ""
    for i in range(3):
        code += random.choice("abcdefghijklmnopqrstuvywz")
    return code
while True:
    num = input("検索回数:")
    data = input("検索ワード:")
    for m in range(int(num)):
        link = image(data)
        download_img(link, code())
        time.sleep(2)
        print("ok")
        if m == int(num):
         break
    print("Finish")
    