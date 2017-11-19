# -*- coding: utf-8 -*-
import requests
from img import imgg
import time


url='https://login.taobao.com'
session_requests=requests.session()
result=session_requests.get(url)
imgg
k=input(u'如果扫完了请输入1：')
if k==1:
    urll='https://taobao.com'
    result=session_requests.get(urll)
    print result.text
else:
    time.sleep(120)



