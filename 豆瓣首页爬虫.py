import requests
from bs4 import BeautifulSoup
link = 'https://movie.douban.com/subject/26366496/?tag=%E7%83%AD%E9%97%A8&from=gaia_video'
movies = []
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
r = requests.get(link,headers=headers,timeout=10)
soup = BeautifulSoup(r.text,'html.parser')
movie_list = soup.find_all('div',class_='indent')
for each in movie_list:
    word = each.find_all('span',property='v:summary')#word --简介（列表）
for a in word:
    b = a.text.strip()
    movies.append(b)
print(movies)
'''for each in movie_list:
    movie_name = each.p.text.strip()
    movies.append(movie_name)
print(movies)'''
