# coding: UTF-8
import requests # urlを読み込むためrequestsをインポート
from bs4 import BeautifulSoup # htmlを読み込むためBeautifulSoupをインポート

URL = 'https://www.google.com/search?q=%E7%8C%AB&tbm=isch&rlz=1C5CHFA_enJP897JP897&hl=ja&ved=2ahUKEwi4hPfn4-7pAhUF7JQKHTyfAUAQBXoFCAEQyAE&biw=1440&bih=789' # URL入力
images = [] # 画像リストの配列

soup = BeautifulSoup(requests.get(URL).content,'lxml') # bsでURL内を解析

for link in soup.find_all("img"): # imgタグを取得しlinkに格納
    if link.get("src").endswith(".jpg"): # imgタグ内の.jpgであるsrcタグを取得
        images.append(link.get("src")) # imagesリストに格納
    elif link.get("src").endswith(".png"): # imgタグ内の.pngであるsrcタグを取得
    	images.append(link.get("src")) # imagesリストに格納

for target in images: # imagesからtargetに入れる
    re = requests.get(target)
    with open('img/' + target.split('/')[-1], 'wb') as f: # imgフォルダに格納
        f.write(re.content) # .contentにて画像データとして書き込む

print("ok") # 確認