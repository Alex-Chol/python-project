import requests
import time
import json
import lxml
import random
adress = input('请输入地址：\n')
link1 = r'https://www.ele.me/restapi/v2/pois?extras[]=count&geohash=ws0e96s8dv52&keyword='
link2 = adress
link3 = r'&limit=20&type=nearby'
link = link1+link2+link3
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
r1 = requests.get(link, headers=headers)
js = json.loads(r1.text)
link_shop = r'https://www.ele.me/restapi/shopping/restaurants?extras[]=activities&geohash='+str(js[0]['geohash'])+r'&latitude='+str(js[0]['latitude'])+r'&limit=24&longitude='+str(js[0]['longitude'])+r'&offset=24&terminal=web'
r2 = requests.get(link_shop,headers=headers)
shop_name = json.loads(r2.text)
print(shop_name)
shop_list = []
for each in range(len(shop_name)):
    shop_list.append(shop_name[each]['name'])
while True:
    shop = random.choice(shop_list)
    print('等下要去的地方是：'+shop)
    a = input('是否前往？Y / N\n')
    if a == 'Y':
        print('祝你用餐愉快！~')
        break
    else:
        continue

