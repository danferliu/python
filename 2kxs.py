import time
import urllib3
import requests
import re
from bs4 import BeautifulSoup

urllib3.disable_warnings()

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

    #try:
    #    r.raise_for_status()
    #except:
    #    print('---url error---')
    #    break

    
    http = urllib3.PoolManager()

    r = http.request('GET',url)
    soup = BeautifulSoup(r.data, "html.parser")
    body = soup.body
    title_1 = body.find('div',id = 'nr_title').string
    
    tag_a = body.find_all('a')
    text_div = body.find_all('div')
    
    
    urlNexta = body.find('a',id = 'pb_next')
    mulu = body.find('a',id = 'pb_mulu')
    urlNext = urlNexta.get('href')
    print ('beging'+ title_1)
    #print (urlNext)
    save_to_file('5.txt',title_1)
    

    textAll = body.find('div',id = 'nr1').text
    save_to_file('5.txt',textAll)
    
    
    #print (soup.prettify)
    print (title_1 + 'end')
    r.release_conn()
    time.sleep(5)
    #print (textAll)
    
    
    
