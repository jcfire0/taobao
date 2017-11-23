# -*- coding: gbk -*-
from login import ojiage,k
import csv
import os
import time
import re


def xingxi(ojiage,k):
    m=[]
    for i in range(0,k):
        b=str(jiage[i])
        p=re.compile(r'\\utffe5')
        q=re.sub(p,'',b)
        m.append(q)


def biaogetou(k):
    h=input(u'如果是第一次爬取的话请输入1，不是就随便输入一个数：')
    if h==1:
        with open('taobao.csv','wb') as f:
                write=csv.writer(f)
                a=[]
                r='日期'
                a.append(r)
                for i in range(1,k+1):
                        p=raw_input(u'请按照给出的顺序输入商品名称:')
                        a.append(p)
                write.writerow(a)
        f.close()
    else:
        with open('taobao.csv','rb') as f:
            reader=csv.reader(f)
            for i,rows in enumerate(reader):
                if i==0:
                    row=rows
                    p=len(row)
            if p!=k+1:
                l=k+1-p
                print u'请手动到表格里添加后'+str(l)+u'项商品名称'
        
        
def shuju(m):
    date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    with open('taobao.csv','ab') as f:
        write=csv.writer(f)
        write.writerow([date]+m)
    f.close()

class main():
    m=xingxi(ojiage,k)
    biaogetou(k)
    shuju(m)
