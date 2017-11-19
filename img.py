# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import requests
import os



def gethtml(url):
    try:
        browser=webdriver.PhantomJS()
        browser.implicitly_wait(10)
        browser.get(url)
        html=browser.page_source
        browser.quit()     #渲染获取动态加载后的网页源代码
        return html
    except:
        print u'网站渲染失败'

def saveimg(html):
    soup=BeautifulSoup(html,'html.parser')
    r=soup.find_all('div',class_="qrcode-img")
    p=str(r)
    po=re.compile('src="(.*?)"/>')
    lianjie=re.findall(po,p)
    urll='http:'+str(lianjie[0])
    try:
        with open('taobao.jpg','wb') as file:
            file.write(requests.get(urll).content)   #把图片写入文件夹中
        print u'二维码保存成功，请快点扫码'
    except:
        print u'图片保存失败'

class imgg():
    url='https://login.taobao.com/'
    html=gethtml(url)
    saveimg(html)
    
    
    


    
