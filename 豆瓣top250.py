import requests
from bs4 import BeautifulSoup
En_name = []
def get_name():
    link = 'https://movie.douban.com/top250'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Host':'https://movie.douban.com/'
    }
    r = requests.get(link,headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')
    name = soup.find_all('div',class_='hd').a.span[2].text.strip()
    print(name)
get_name()