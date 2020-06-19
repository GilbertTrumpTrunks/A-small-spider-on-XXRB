import requests
user_agent='Gecko/20100101 Firefox/70.0'
headers={'User-Agent':user_agent}
Dat=open('Date.txt','r')
import csv
import re
from bs4 import BeautifulSoup as bs
for date in Dat:
    f_url=open('rb'+str(date)[0:4]+'.txt','r')
    rows=[]
    for url_suf in f_url:
        rebds=re.compile(r'./2019[01]\d/t2019'+str(date)[0:4]+'_\d+.htm')
        p=rebds.findall(url_suf)
        cont=0
        for suf in p:
            url='http://epaper.xmnn.cn/xmrb/2019'+str(date)[0:4]+'/'+str(suf)[2:-3]+'htm'
            print(url)
            r=requests.get(url,headers=headers)
            r.encoding=r.apparent_encoding
            path='F:/XMRB/Article/'
            hanzi=re.compile('[\u4e00-\u9fa5\u3002\uff1f\uff01\uff0c\u3001\uff1B\uff1a\u300c-\u300f\u2019\u2019\u201c\u201d\uff08\uff09\u3014\u3010\u3015\u3011\u2014\u2026\u2013\uff0e\u300a\u300b\u3008\u3009]+')
            page=bs(r.text,'html.parser',from_encoding=r.apparent_encoding)            
            s= open (path+str(date)[0:4]+'_'+str(cont)+'.txt','w')
            for x in page.find_all('p'):
                    stringg=x.get_text()
                    c=hanzi.findall(stringg)
                    for han in c:
                        s.write(han)
            s.close()
            cont+=1
                    
                    
                    
