import requests
import lxml
import time
from bs4 import BeautifulSoup
import csv
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
link = r'https://beijing.anjuke.com/sale/' 
'''
房源列表    li.list-item    √
二手房源名称    div.house-title>a   √
价格    div.pro-price>span.price-det    
几房几厅    div.details-item>span  第一个
大小    div.details-item>span  第二个
建造年份    div.details-item>span  第四个
联系人  div.details-item>span.brokername
地址    span.comm-address
标签    div.tags-bottom>span (多个span标签)
'''
r = requests.get(link,headers=headers)
soup = BeautifulSoup(r.text,'lxml')
house = soup.select('li.list-item')
for each in house:
    name = each.find('div',class_='house-title')
    name = name.a.text.strip()
    price = each.find('div',class_='pro-price')
    price = price.span.text
    room = each.find('div',class_='details-item').span
    room = room.text
    width = each.find('div',class_='details-item').span.next_sibling.next_sibling
    width = width.text
    build_year = each.find('div',class_='details-item').span.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
    build_year = build_year.text
    connect = each.find('div',class_='details-item')
    connect = connect.find('span',class_='brokername').text.split('')[1]
    adress = each.find('span',class_='comm-address')
    adress = adress.text.strip().split('\n')  # --->里面有\n
    adress = ' '.join(adress)
    tags = each.find('div',class_='tags-bottom')
    litter_tag = tags.find_all('span')
    tag_list = []
    for each_tag in litter_tag:
        tag_list.append(each_tag.text)
    tag = ' '.join(tag_list)
    house_list = [name,price,room,width,build_year,connect,adress,tag]
    with open('D://Anjuke.csv','w+',encoding='UTF-8',newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerow(house_list)
print('begin!')

