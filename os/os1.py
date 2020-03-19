import requests
import csv
import time

headers={
'Cookie': '118247"; bid=ZmLBefMrdSY; _vwo_uuid_v2=D8328065DA6EFABE891498524AEA116C9|bc93ce315aae7ce5670d8387a48374dc; douban-fav-remind=1; __yadk_uid=RIYJbS1TArCPIepeGpsFpPOvcsArt4FP; trc_cookie_storage=taboola%2520global%253Auser-id%3D3011df8b-37d5-479d-aa52-c558d2d55d25-tuct3f72b7d; __gads=ID=d42cc7ac0b20cba0:T=1565224898:S=ALNI_MbG0a_E-eLkeIvBumqrNM52T55r3A; viewed="5336893"; gr_user_id=d6d31e04-4990-4d05-a43e-504efb65a32b; __utmv=30149280.20357; douban-profile-remind=1; push_noty_num=0; push_doumail_num=0; ct=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1572272336%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utmc=30149280; __utma=223695111.1698974020.1562999988.1572170557.1572272336.39; __utmb=223695111.0.10.1572272336; __utmc=223695111; __utmz=223695111.1572272336.39.29.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=30149280.688340515.1550546482.1572272336.1572272341.53; __utmz=30149280.1572272341.53.40.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; dbcl2="203576406:2/bg4WcMeNU"; ck=kA7Q; __utmb=30149280.3.10.1572272341; _pk_id.100001.4cf6=3aee40e01a3c897b.1562999988.36.1572272526.1572170742.',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}
outpath='url.csv'
with  open(outpath,'w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([''])
start = time.time()
for i in range(0,800,20):
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
end = time.time()
print("用时"+str(end-start))
