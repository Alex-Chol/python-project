import requests
from bs4 import BeautifulSoup
link = 'https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=pencil'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
r = requests.get(link,headers=headers)
results = []
prices = []
soup = BeautifulSoup(r.text,'html.parser')#tag
h2 = soup.find_all('h2',class_='title')#list  h2[0].a.text --->铅笔名
price = soup.find_all('div',class_='price')
#for each in num:
#    print(each.text)
for i in price:
    a = i.b.contents
    prices.append(a[0].strip())
for each in range(0,len(prices)):
    result = 'result'+str(each)
    result = {'name':h2[each].a.text,'price':prices[each]}
    results.append(result)
for i in results:
    print(i)