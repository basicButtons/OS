import csv
import re
import os
from bs4 import BeautifulSoup
import threading
import time
import requests

outpath1 = "url1.csv"
outpath2 = "url2.csv"
outpath3 = "url3.csv"
outpath4 = "url4.csv"

headers={
'Cookie': '118247"; bid=ZmLBefMrdSY; _vwo_uuid_v2=D8328065DA6EFABE891498524AEA116C9|bc93ce315aae7ce5670d8387a48374dc; douban-fav-remind=1; __yadk_uid=RIYJbS1TArCPIepeGpsFpPOvcsArt4FP; trc_cookie_storage=taboola%2520global%253Auser-id%3D3011df8b-37d5-479d-aa52-c558d2d55d25-tuct3f72b7d; __gads=ID=d42cc7ac0b20cba0:T=1565224898:S=ALNI_MbG0a_E-eLkeIvBumqrNM52T55r3A; viewed="5336893"; gr_user_id=d6d31e04-4990-4d05-a43e-504efb65a32b; __utmv=30149280.20357; douban-profile-remind=1; push_noty_num=0; push_doumail_num=0; ct=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1572272336%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utmc=30149280; __utma=223695111.1698974020.1562999988.1572170557.1572272336.39; __utmb=223695111.0.10.1572272336; __utmc=223695111; __utmz=223695111.1572272336.39.29.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.688340515.1550546482.1572272336.1572272341.53; __utmz=30149280.1572272341.53.40.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; dbcl2="203576406:2/bg4WcMeNU"; ck=kA7Q; __utmb=30149280.3.10.1572272341; _pk_id.100001.4cf6=3aee40e01a3c897b.1562999988.36.1572272526.1572170742.',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}

with open(outpath1, mode='w', newline='', encoding="utf-8-sig") as infile:
    write = csv.writer(infile)
    write.writerow('')
with open(outpath2, mode='w', newline='', encoding="utf-8-sig") as infile:
    write = csv.writer(infile)
    write.writerow('')
with open(outpath3, mode='w', newline='', encoding="utf-8-sig") as infile:
    write = csv.writer(infile)
    write.writerow('')
with open(outpath4, mode='w', newline='', encoding="utf-8-sig") as infile:
    write = csv.writer(infile)
    write.writerow('')

def one():
    for i in range(0,200,20):
        params = {
        "sort": "U",
        "range": "0,10",
        "tags":"",
        "start": str(i),
        "year_range": "2018,2018"
        }
        url = 'https://movie.douban.com/j/new_search_subjects'
        res = requests.get(url,headers=headers,params=params)
        json_list = res.json()
        items = json_list['data']
        for item in items:
            url = item['url']
            with  open(outpath1,'a',newline='',encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([i,url])
    

def two():
    for i in range(200,400,20):
        params = {
        "sort": "U",
        "range": "0,10",
        "tags":"",
        "start": str(i),
        "year_range": "2018,2018"
        }
        url = 'https://movie.douban.com/j/new_search_subjects'
        res = requests.get(url,headers=headers,params=params)
        json_list = res.json()
        items = json_list['data']
        for item in items:
            url = item['url']
            with  open(outpath2,'a',newline='',encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([i,url])
                
def three():
    for i in range(400,600,20):
        params = {
        "sort": "U",
        "range": "0,10",
        "tags":"",
        "start": str(i),
        "year_range": "2018,2018"
        }
        url = 'https://movie.douban.com/j/new_search_subjects'
        res = requests.get(url,headers=headers,params=params)
        json_list = res.json()
        items = json_list['data']
        for item in items:
            url = item['url']
            with  open(outpath3,'a',newline='',encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([i,url])

def four():
    for i in range(600,800,20):
        params = {
        "sort": "U",
        "range": "0,10",
        "tags":"",
        "start": str(i),
        "year_range": "2018,2018"
        }
        url = 'https://movie.douban.com/j/new_search_subjects'
        res = requests.get(url,headers=headers,params=params)
        json_list = res.json()
        items = json_list['data']
        for item in items:
            url = item['url']
            with  open(outpath4,'a',newline='',encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([i,url])
#111,1566,2090 2270 2496 2704 3079 3143 3377 3944 4027 4034 4355 4424
#5178 5364 5437 5609 6131 6367 7142 7239 7285 7393 7449 7479
#7826 8107 8474 9069 9370 9765
start = time.time()
t1 = threading.Thread(target=one)
t2 = threading.Thread(target=two)
t3 = threading.Thread(target=three)
t4 = threading.Thread(target=four)
t1.start()
t2.start()
t3.start()
four()
end = time.time()
print(end- start)