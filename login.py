# -*- coding: utf-8 -*-
from selenium import webdriver
import os
from bs4 import BeautifulSoup
import re


name=raw_input(u'请输入账号:')
password=raw_input(u'请输入密码:')
bro=webdriver.Chrome()
bro.implicitly_wait(10)
bro.get('https://login.taobao.com/')
bro.find_element_by_id('J_Quick2Static').click()
bro.find_element_by_id('TPL_username_1').clear()
bro.find_element_by_id('TPL_username_1').send_keys(name)
bro.find_element_by_id('TPL_password_1').clear()
time.sleep(4)
bro.find_element_by_id('TPL_password_1').send_keys(password)
time.sleep(20)
bro.find_element_by_id('J_SubmitStatic').click()
handle=bro.current_window_handle
bro.find_element_by_id('J_MiniCart').click()
handle=bro.current_window_handle
html=bro.page_source           #这几行代码是通过selenium模拟鼠标和键盘的操作来实现进入自己的购物车界面
soup=BeautifulSoup(html,'html.parser')
r=soup.find_all('a',class_="item-title J_MakePoint")
mi=str(r)
mii=re.compile('>(.*?)</a>')
minzi=re.findall(mii,mi)
rr=soup.find_all('em',class_="price-original")
pr=str(rr)
prr=re.compile('>(.*?)</em>')
jiujia=re.findall(prr,pr)
j=soup.find_all('em',class_="J_Price price-now")
ji=str(j)
jia=re.compile('>(.*?)</em>')
jiage=re.findall(jia,ji)
k=len(minzi)            #通过美味汤解析购物车网页，把商品的名字，原价，现价等数据采集下来

ominzi=[]
ojiujia=[]
ojiage=[]
for i in range(0,k):
    ominzi.append(minzi[k-i-1])
    ojiujia.append(jiujia[k-i-1])
    ojiage.append(jiage[k-i-1])
    print (str(i)+'    '+ominzi[i].decode('unicode_escape')+'   '+u'原价:'+ojiujia[i].decode('unicode_escape')+'   '+u'现价:'+ojiage[i].decode('unicode_escape'))
#因为购物车爬下来最新添加的是第一个，这几行代码是将顺序反一下，让最新添加的商品放在后面
