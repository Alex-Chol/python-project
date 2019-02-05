import requests
import json
link = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
r = requests.get(link,headers=headers)#成功运行
r.encoding = 'utf-8'
json_data = json.loads(r.text)
print(type(json_data)
commnt_list = json_data['subjects']['title']
print(commnt_list)
#for each in commnt_list:
#    message = commnt_list[each]['title']
#    print(message)
#for i in range(0,len(json_data['data'])):
#    print(json_data['data'])