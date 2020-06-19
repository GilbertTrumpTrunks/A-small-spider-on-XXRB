import requests
user_agent='Gecko/20100101 Firefox/70.0'
headers={'User-Agent':user_agent}
Dat=open('Date.txt','r')
import csv
import re
from bs4 import BeautifulSoup as bs
def work():
        for line in Dat:
                eline=line[0:4]
                url='http://epaper.xmnn.cn/xmrb/2019'+str(eline)+'/'
                r=requests.get(url,headers=headers)
                r.encoding=r.apparent_encoding
                path='F:/XMRB/xmrb'+str(eline)
                fil='F:/XMRB/xmrb'+str(eline)+'.html'
        #	with open(fil,'w',encoding=r.apparent_encoding)as f:
        #		f.write(r.text)
                rebds=re.compile(r'./2019[01]\d/t[0-9_]+.htm')
                rebds.findall(r.text)
                rows=[]
                p=bs(r.text,'html.parser',from_encoding=r.apparent_encoding)
                print(p.title)
                contents=p.find_all(href=re.compile(r'./2019[01]\d/t[0-9_]+.htm'))
                for content in contents:
                        href=content.get('href')
                        row=(content.string,href)
                        rows.append(row)
                with open('F:/XMRB/rb'+str(eline)+'.csv','w',encoding='gb18030')as f:
                        f_csv=csv.writer(f)
                        f_csv.writerows(rows)
                f.close()      
                with open('F:/XMRB/rb'+str(eline)+'.txt','w')as F:
                        for i in range(len(rows)):
                                F.writelines(rows[i])
                                F.writelines('\n')
                F.close()
work()
