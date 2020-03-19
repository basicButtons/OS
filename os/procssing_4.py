import csv
import re
import os
from bs4 import BeautifulSoup
import multiprocessing
import time


outpath = "/Users/maxuan/Desktop/1/test.csv"
mulu = ('id', '电影名', '导演', '编剧', '主演', '类型', '地区', '语言', '日期', '片长', '又名', 'IMDB', '评论人', '评论时间','评论内容', '星级', '有用数','评分','人数')
'''
with open(outpath, mode='w', newline='', encoding="utf-8-sig") as infile:
    write = csv.writer(infile)
    write.writerows(mulu)

'''
def lenJ(list):
    if len(list) > 1:
        res = str(list[0])
        for i in range(1,len(list)):
            res = res +'+'+str(list[i])
    elif len(list) == 1:
        res = str(list[0])
    else:
        res = None
    return res
def pinglunJ(list):
    if len(list) > 1:
        res = [list[0]]
        for i in range(1,len(list)):
            res = res + '{{马轩}}' +list[i]
    elif len(list) == 1:
        res = list[0]
    else:
        res = None
    return res
def pinglunJION(list):
    if len(list) > 1:
        res = str(list[0])
        for i in range(1,len(list)):
            res = res + "{{马轩}}" + str(list[i])
    elif len(list) == 1:
        res = str(list[0])
    else:
        res = None
    return res

def parser(txt):
    with open("/Users/maxuan/Desktop/1/txt/"+ txt,"r",encoding="utf-8") as f:
        txt = f.read()
        res=[]
        id = txt.split('.')[0]
        soup = BeautifulSoup(txt,'html.parser')
        name  = soup.find('span',{'property':"v:itemreviewed"}).get_text()
        #print(name)
        daoyan = re.findall('<a href=".*?" rel="v:directedBy">(.*?)</a>', txt, re.M)
        daoyan = lenJ(daoyan)
        #导演 daoyan
        temptxt = re.findall('编剧</span>(.*?)</span>', txt, re.M)
        if len(temptxt) > 0:
            bianju = re.findall('<a href=".*?">(.*?)</a>',temptxt[0])
            bianju = lenJ(bianju)
        else:
            bianju = None
                   
        #print(bianjujures)
        #
        zhuyanlist = re.findall('<a href="/celebrity/.*?" rel="v:starring">(.*?)</a>', txt, re.M)
        zhuyan = lenJ(zhuyanlist)
                   
                   
        leixing = re.findall('<span property="v:genre">(.*?)</span>',txt, re.M)
        leixing = lenJ(leixing)
        # print(leixing)
        try:
            diqu = re.findall(' <span class="pl">制片国家/地区:</span>.(.*?)<br/>',txt,re.M)[0]
        except IndexError:
            diqu =None
        yuyan = re.findall(' <span class="pl">语言:</span>.(.*?)<br/>',txt,re.M)
        yuyan = lenJ(yuyan)
        
        riqi = re.findall(' <span property="v:initialReleaseDate" content="(.*?)">',txt,re.M)
        riqi  = lenJ(riqi)
        
        pianchang = re.findall(' <span property="v:runtime" content="(.*?)">',txt,re.M)
        pianchang = lenJ(pianchang)
        
        youming = re.findall(' <span class="pl">又名:</span>.(.*?)<br/>',txt,re.M)
        youming =  lenJ(youming)
        
        IMDB = re.findall(' <span class="pl">IMDb链接:</span> <a href="(.*?)"',txt,re.M)
        IMDB = lenJ(IMDB)

        pingluninfo = soup.find('div',{"id": "hot-comments"})
        try:
            pinglunitems = pingluninfo.find_all('div',class_ = "comment-item")
            if len(pinglunitems) > 0:
                pinglunren = []
                pinglunshijian = []
                pinglunneirong = []
                youyongshu = []
                for item in pinglunitems:
                    pinglunren.append(item.find("span",{"class":"comment-info"}).find("a").get_text())
                    pinglunshijian.append(item.find("span",{"class":"comment-time"})['title'])
                    pinglunneirong.append(item.find("span",{"class":"short"}).get_text())
                    youyongshu.append(item.find("span",class_="votes").get_text())
            if len(pinglunitems) == 0:
                pinglunren = None
                pinglunshijian = None
                pinglunneirong = None
                youyongshu  = None
            pinglunneirong = pinglunJION(pinglunneirong)

            pinglunshijian = pinglunJION(pinglunshijian)

            pinglunren = pinglunJION(pinglunren)
            youyongshu = pinglunJION(youyongshu)
        except AttributeError:
            pinglunren = None
            pinglunshijian = None
            pinglunneirong = None
            youyongshu = None
        xingji = re.findall('  <span class="allstar(.)0 rating"',txt,re.M)
        xingji = lenJ(xingji)
        
        pingfen =re.findall('  <strong class="ll rating_num" property="v:average">(.*?)</strong>',txt,re.M)
        if len(pingfen) > 0:
            pingfen = pingfen[0]
        else:
            pingfen = None

        renshu = re.findall('  <span property="v:votes">(.*?)</span>',txt,re.M)
        renshu = lenJ(renshu)
        
# while response.status_code==200 :
#     response = response.text
#     break
# else:
#         response = s.get(url, timeout=60.03)
#         response = response.text
        res.append([id, name,daoyan,bianju,zhuyan,leixing,diqu,yuyan,riqi,pianchang,youming,IMDB,pinglunren,pinglunshijian,pinglunneirong,xingji,youyongshu,pingfen,renshu])
# print([url[0], response.text])

        with open(outpath, mode='a', newline='', encoding="utf-8-sig") as infile:
            write = csv.writer(infile)
            write.writerows(res)

dirs="/Users/maxuan/Desktop/1/txt"
mylist = os.listdir(dirs)

def process(start,length):
    for i in range(start-1,start + length - 1):
        if i in [111,1566,2089,2269,2495,2703,3077,3141,3375,3942-1,4025-1,4032-1,4353-2,4422-2,5176-2,5362-2,5435-2,5607-2,6127,6165-2,6365-2,7140-4,7237-4,7283-4,7391-5,7447-5,7477-5,7824-7,8105-7,8472-8,9067-7,9368-7,9761-7,7658,7815]:
            continue
        print(i)
        parser(mylist[i])
    
if __name__ == '__main__':
    multi_start = time.time()    
    p1 = multiprocessing.Process(target=process,args=(1,200))
    p2 = multiprocessing.Process(target=process,args=(201,200))
    p3 = multiprocessing.Process(target=process,args=(401,200))
    p1.start()
    p2.start()
    p3.start()
    process(601,200)
    multi_end = time.time()
    print('\nMulti process cost time:', multi_end - multi_start)