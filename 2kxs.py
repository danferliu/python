import time
import urllib3
import requests
import re
from bs4 import BeautifulSoup

def save_to_file(file_name, contents):
    fh = open(file_name, 'a',encoding='utf-8')
    fh.write(contents)
    fh.writelines("\n")
    fh.close()
    return 'success'

urlNext = '/book/97286/25517067.html'
   
while urlNext != '/book/97286/':
    urlBas = 'https://m.fpzw.com'
    url = urlBas + urlNext
    #print (url)
    http = urllib3.PoolManager()
    
    try:
        url.raise_for_status()
    except:
        print('---error---')
    r = http.request('GET',url)
    soup = BeautifulSoup(r.data, "html.parser")
    body = soup.body
    title_1 = body.find('div',id = 'nr_title').string
    
    tag_a = body.find_all('a')
    text_div = body.find_all('div')
    
    
    urlNexta = body.find('a',id = 'pb_next')
    mulu = body.find('a',id = 'pb_mulu')
    urlNext = urlNexta.get('href')
    print ('开始'+ title_1)
    #print (urlNext)
    save_to_file('抗日之特战兵王5.txt',title_1)
    

    textAll = body.find('div',id = 'nr1').text
    save_to_file('抗日之特战兵王5.txt',textAll)
    
    
    #print (soup.prettify)
    print (title_1 + '结束')
    time.sleep(35)
    #print (textAll)
    
    
    
