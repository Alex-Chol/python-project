import requests
from bs4 import BeautifulSoup
def get_movies():
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Host':'movie.douban.com'}
    movie_list = []
    for i in range(0,1):
        if i == 0:
            link = 'https://movie.douban.com/top250'
        else:
            link = 'https://movie.douban.com/top250?start='+str(i*25)+'&filter='
        r = requests.get(link,headers=headers,timeout=10)
        print(str(i+1)+'页状态码'+str(r.status_code))
        soup = BeautifulSoup(r.text,"xml")
        div_list = soup.find_all('div',class_='hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
        #  .next_sibling  获取兄弟节点
        # soup.a.next_sibling
    return movie_list
movies = get_movies()              
