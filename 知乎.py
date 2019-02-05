import requests
from bs4 import BeautifulSoup
import json
import csv
from urllib.request import quote
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Host':'api.zhihu.com',
    'origin':'https://www.zhihu.com',
    'Referer':'https://www.zhihu.com/lives',
    'Connection':'keep-alive'
    
}
subject_list = []
live_links = []
lives_id = []
def main():
    link = 'https://api.zhihu.com/lives/homefeed?includes=live'
    r = requests.get(link,headers=headers)
    js = json.loads(r.text)
    while True:
        data = js['data']
        for each in range(len(data)):
            title = data[each]['live']['subject']
            name = data[each]['live']['speaker']['member']['name']
            score = data[each]['live']['review']['score']
            people = data[each]['live']['seats']['taken']
            live_id = data[each]['live']['id']
            live_link = 'https://api.zhihu.com/lives/'+str(live_id)
            subject_list.append(title)
            live_links.append(live_link)
            lives_id.append(live_id)
            print(title)
            # 进一步进行保存操作
            with open('D://zhihu.csv','a+',encoding='UTF-8',newline='') as csvfile:
                w = csv.writer(csvfile)
                w.writerow([title,name,score,people,live_link])
        print('--------------------------------')
        if not js['paging']['is_end']:
            next_link = js['paging']['next']
            r = requests.get(next_link,headers=headers)
            js=json.loads(r.text)
        else:
            break
#'paging': {'is_end': False, 'next': 'https://api.zhihu.com/lives/homefeed?limit=10&offset=10', 
link_lists = []
a = 1
def second_main(link_list,arg):
    new_links = link_list
    link_lists = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    for each in new_links:
        link = each+'/related'
        #   ?limit=5&offset=5
        r = requests.get(link,headers=headers)
        js = json.loads(r.text)        
        while True:#某一个live页面里
            data = js['data']
            for each_1 in range(len(data)):
                title = data[each_1]['subject']
                name = data[each_1]['speaker']['member']['name']
                score = data[each_1]['review']['score']
                people = data[each_1]['seats']['taken']
                live_id2 = data[each_1]['id']
                live_link = 'https://www.zhihu.com/lives/'+str(live_id2)
                if live_id2 not in lives_id and live_link not in new_links:
                    subject_list.append(title)
                    live_links.append(live_link)
                    link_lists.append(live_link)
                    '''with open('D://zhihu.csv','a+',encoding='UTF-8',newline='') as csvfile:
                        w = csv.writer(csvfile)
                        w.writerow([title,name,score,people,live_link])'''
                print(subject_list[-1])
                if not js['paging']['is_end']:
                    next_link = js['paging']['next']
                    r = requests.get(next_link,headers=headers)
                    js=json.loads(r.text)
                print('-------------------------------------------')    
            else:
                break
        if arg != 3:
            arg += 1
            print('第'+str(arg)+'次爬取')
            second_main(link_lists,arg)
        else:
            print('程序已运行完毕!')
            exit()

main()
second_main(live_links,a)
