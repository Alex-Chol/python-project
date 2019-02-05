import requests
from bs4 import BeautifulSoup
from tkinter import *
main_link = 'https://www.dy2018.com/e/search/index.php'

headers2 = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
#main(main_link,keyborad)
'''cookies_download ={
    'Hm_lvt_a68dc87e09b2a989eec1a0669bfd59eb':'1545215743,1545564289,1545578872,1545652320',
    'gr_user_id':'0b0b376e-5121-4452-82ba-697cefd636b6',
    '_ga':'GA1.2.1210606602.1545100429',
    'pescdlastsearchtime':'1545623593',
    'XLA_CI':'ca32b4999003c7bc698f8d63de4f61c7',
    'gr_session_id_bce67daadd1e4d71':'c0657032-32a3-4ee8-bb97-8b00d07767b3',
    'gr_session_id_bce67daadd1e4d71_c0657032-32a3-4ee8-bb97-8b00d07767b3':'true',
    'Hm_lpvt_a68dc87e09b2a989eec1a0669bfd59eb':'1545652333',
    'myad':'1'
}'''
def movie_haven(link,key,t1):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Origin':'https://www.dy2018.com',
            'Referer':'https://www.dy2018.com/',
            'Cookie':'grwng_uid=6f0c3b8f-1740-494c-8b63-6fc657d5022c'}
        data = {
        'Submit':'立即搜索',
        'classid':'0',
        'show':'title,smalltext',
        'tempid':'1',
        'keyboard':key
        }
        t1.delete('1.0','end')
        r = requests.post(link,headers=headers,data=data)
        r = r.content.decode('gb2312','ignore')
        soup = BeautifulSoup(r,'html.parser')
        title_list = soup.select('div.co_content8 ul table.tbspan')
        #print(title_list)
        #print(str(len(title_list))+'个结果')
        t1.insert(END,'------------------------------------------------------------------\n')
        t1.insert(END,'                        '+str(len(title_list))+'个结果\n')
        t1.insert(END,'------------------------------------------------------------------\n\n')
        for each in title_list:
            a = each.select('a.ulink')
            title_name = a[0].get('title')
            movie_link = 'https://www.dy2018.com'+a[0].get('href')
            #print(title_name)
            t1.insert(END,title_name+'\n')
            get_download_link(movie_link,t1)
            t1.insert(END,'-------------------------------------------\n\n')
def get_download_link(link_,text):
    r = requests.get(link_,headers=headers2)
    r = r.content.decode('gb2312','ignore')
    soup = BeautifulSoup(r,'html.parser')
    s = soup.select('div#Zoom tbody a')
    if s:
        a = 1
        for each_down_link in s:
            download_link = each_down_link.get('href')
            text.insert(END,'第'+str(a)+'个下载地址：\n'+download_link+'\n')
            a += 1
            #print(download_link)

    else:
        text.insert(END,'这个链接获取出错或者没有下载链接~\n')
