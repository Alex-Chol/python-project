import requests
from bs4 import BeautifulSoup
link = 'https://movie.douban.com/top250'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
movies_list = []
r = requests.get(link,headers=headers)
soup = BeautifulSoup(r.text,'html.parser')
movie_name = soup.find_all('div',class_='hd')#先爬出 电影名字。再爬出导演名，编成字典导入列表
daoyan_name = soup.find_all('p',class_='')#导演
for each in range(0,len(movie_name)):
    movie_dict_name = 'movie_dict'+str(each)
    movie_dict_name = {'name':movie_name[each].a.span.text.strip(),'daoyan':daoyan_name[each].text.strip()}
    movies_list.append(movie_dict_name)
for each in movies_list:
    print(each)