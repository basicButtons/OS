import multiprocessing
import time
import requests
import csv
headers={
'Cookie': 'll="118247"; bid=ZmLBefMrdSY; _vwo_uuid_v2=D8328065DA6EFABE891498524AEA116C9|bc93ce315aae7ce5670d8387a48374dc; douban-fav-remind=1; __gads=ID=d42cc7ac0b20cba0:T=1565224898:S=ALNI_MbG0a_E-eLkeIvBumqrNM52T55r3A; viewed="5336893"; gr_user_id=d6d31e04-4990-4d05-a43e-504efb65a32b; __utmv=30149280.20357; douban-profile-remind=1; push_noty_num=0; push_doumail_num=0; ct=y; __utmc=30149280; __utmz=30149280.1572315793.56.42.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=30149280.688340515.1550546482.1572315793.1572323449.57; dbcl2="203576406:4LUdB3Xb8Z0"; ck=j5BX; __utmt=1; __utmb=30149280.5.10.1572323449; frodotk="3f95090044f9de01bebf1b00ceed9a03"'
}
outpath='urlByXieCheng.csv'
'''
with  open(outpath,'w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([''])
start = time,time()
'''
def requests1():
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
            with  open(outpath,'a',newline='',encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([i,url])
def requests2():
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
            with  open(outpath,'a',newline='',encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([i,url])
def requests3():
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
            with  open(outpath,'a',newline='',encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([i,url])

def requests4():
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
            with  open(outpath,'a',newline='',encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([i,url])


if __name__ == '__main__':
    multi_start = time.time()
    p1 = multiprocessing.Process(target=requests1)
    p2 = multiprocessing.Process(target=requests2)
    p3 = multiprocessing.Process(target=requests3)
    p1.start()
    p2.start()
    p3.start()
    requests4()
    multi_end = time.time()
    print('\nMulti process cost time:', multi_end - multi_start)
