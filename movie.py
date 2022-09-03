# import the package
import pickletools
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import etree
import os
# define the value
start=0
result=[]
header={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}

def downloadimg(src,id):
    # you have to add "/" afte the path, so the image can be under that folder
    # downloadImgs = "/Users/glenn/Downloads/python/downloadImgs/"
    dir= './downloadImgs/' + str(id) 
    try:
        pic=requests.get(src,timeout=10)
    except requests.exceptions.ConnectionError:
        print("image download error")

    fp = open(dir,'wb')
    fp.write(pic.content)
    fp.close()


# single page donwload
# url = requests.get('https://movie.douban.com/celebrity/1166896/photos/?type=C&start=' + str(start) + '&sortby=like&size=a&subtype=a',headers=header)
# soup=BeautifulSoup(url.text,'html.parser')
# How to use Xpath with BeautifulSoup ?
# https://www.geeksforgeeks.org/how-to-use-xpath-with-beautifulsoup/
# dom=etree.HTML(str(soup))
# img="/html[@class='ua-mac ua-webkit']/body/div[@id='wrapper']/div[@id='content']/div[@class='grid-16-8 clearfix']/div[@class='article']/ul[@class='poster-col3 clearfix']/li/div[@class='cover']/a/img/@src"
# imgs = dom.xpath(img)
# for img in imgs:
#     print(img,imgs.index(img))
#     id=imgs.index(img)
#     downloadimg(img,id)

# for loop to scale the single logic
for i in range(0,90,30):
    # start= 0 30 picks
    # start= 30 60 pisc
    # start=60 90 pics
    # get the structure of the website
    html = requests.get('https://movie.douban.com/celebrity/1166896/photos/?type=C&start=' + str(i) + '&sortby=like&size=a&subtype=a',headers=header)
    html.encoding='utf-8'
    # start+=25
    soup=BeautifulSoup(html.text,'html.parser')
    # use the bs4 to trieve the target data
    dom=etree.HTML(str(soup))
    img="/html[@class='ua-mac ua-webkit']/body/div[@id='wrapper']/div[@id='content']/div[@class='grid-16-8 clearfix']/div[@class='article']/ul[@class='poster-col3 clearfix']/li/div[@class='cover']/a/img/@src"
    imgs = dom.xpath(img)
    for img in imgs:
        # id = imgs.index(img)+1
        # Python | Extract words from given string
        # https://www.geeksforgeeks.org/python-extract-words-from-given-string/
        res = img.split("/")
        name = res[7]
        # name2 = name.split(".")
        print(img,name)       
        downloadimg(img,name)

# print(dom.xpath(img))  

# print(result)
# excle format the data
# df = pd.DataFrame(result)
# # conver the data into excelsheet to view it
# df.to_excel("Craw 豆瓣网评分最高的250部电影.xlsx")