import requests
from bs4 import BeautifulSoup
import urllib.request
import os,sys
import time
import random

def save_images(num_pages,query_word):
    headers={"User-Agent": "hoge"}
    for i in range(num_pages):
        URL="https://search.yahoo.co.jp/image/search?p={0}&rkf=1&dim=&ctype=face&imw=0&imh=0&imc=&ei=UTF-8&b={1}".format(query_word,1+20*num_pages)
        resp=requests.get(URL,timeout=1,headers=headers)
        soup=BeautifulSoup(resp.text,"lxml")
        
        elems=soup.find_all(alt="「{}」の画像検索結果".format(query_word))

        if not os.path.exists("./dataset/validation/"+query_word):
            os.makedirs("./dataset/validation/"+query_word)

        for (index,e) in enumerate(elems):
            filepath="./dataset/validation/{0}/{1}-{2}.jpg".format(query_word,str(i),str(index))
            if os.path.exists(filepath): continue   
            urllib.request.urlretrieve(e["src"],filepath)
        
        sys.stdout.write("\rDownloading...{0}/{1}".format(i,num_pages))
        sys.stdout.flush()
        time.sleep(1+random.random())

def main():
    num_pages=int(sys.argv[1])
    query_word=sys.argv[2]

    save_images(num_pages,query_word)

    print("Done. {0} / {1}".format(num_pages,num_pages))

if __name__=="__main__":
    main()
