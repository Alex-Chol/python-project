import requests
from bs4 import BeautifulSoup
title = []
def santostang():
    link = 'https://www.ele.me/place/ws0eqm8bet27?latitude=23.101616&longitude=113.478964'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    }
    r = requests.get(link,headers=headers)
    soup = BeautifulSoup(r.text,'html.parser') 
    print(soup)
    return 0
begin = santostang()
