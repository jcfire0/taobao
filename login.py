# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os


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
time.sleep(120)
bro.find_element_by_id('J_SubmitStatic').click()
now_url=bro.current_url
print now_url


