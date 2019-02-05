import requests
from bs4 import BeautifulSoup
from urllib.request import quote
from tkinter import *
def yangguang(movie_name,text1):
    try:
        text1.delete('1.0','end')
        movie_code = movie_name.encode('gbk')
        link = r'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(movie_code)
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
        r1 = requests.get(link,headers=headers)
        soup1 = BeautifulSoup(r1.text,'html.parser')
        movies = soup1.select('div.co_content8 ul table b a')
        movie_list = []
        for each in movies:
            link2 = r'https://www.ygdy8.com'+each.get('href')
            movie_list.append(link2)
        a = 1
        for each in movie_list:
            r3 = requests.get(each,headers=headers).content.decode('gbk')
            soup3 = BeautifulSoup(r3,'html.parser')
            name = soup3.select('div.title_all h1 font')
            name = name[0].text
            #print(str(a)+'、'+name)
            text1.insert(END,str(a)+'、'+name+'\n')
            download = soup3.select('div.co_content8 table tbody tr td a')
            for i in range(len(download)):
                text1.insert(END,download[i].get('href')+'\n\n')
                #print(download[i].get('href'))
                #print('\n')
            a += 1
        #return 'Running Successful'
    except UnicodeDecodeError:
        print('编码错误，请重试\n')
#name = input('输入电影名:\n')
#start_yangguang = yangguang(name)
#print(start_yangguang)


