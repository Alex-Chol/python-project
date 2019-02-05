import requests
from bs4 import BeautifulSoup
import json
import re
import csv
cookie1 = {
    '__utma':'155987696.1525777342.1545196969.1545196969.1545231689.2',
    '__utmz':'155987696.1545196969.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '_xsrf':'XSDisAOoCNR1OLGVtQhRka2KxSfcptr1',
    '_zap':'13ce7960-3fce-4822-92a6-7af5ca30389e',
    'cap_id':"MmU4MDBiZGU1ODlmNDg3Y2E5MzNmMWJlOTYxNjQyOGQ=|1545380300|0fb966042c4111296df060e3170fe893eb810e58",
    'capsion_ticket':"2|1:0|10:1545380317|14:capsion_ticket|44:YmVmNDQ3ZTViMDg1NGFjYjg1NjExYTM4YjA4YWY1YzM=|d0caca466fb583a76406e6b56b4b740cbd6b374df9fe4ca9e78a1a9072b879cc",
    'd_c0':"AKCgIQdKsQ6PTm7RQYWtvtdkh-t274iFX6w=|1545195843",
    'l_cap_id':"ZjZiMjYyYjUzNzM4NGM5Yjk4NzQwNDI5OGZlN2FkN2M=|1545380300|a66dbf3e7cce5f462d62cbaa6dc895b5c38d3b62",
    'q_c1':'91e4406affba4f999947fa7ff05200d3|1545195969000|1545195969000',
    'r_cap_id':"NjAxYTYxZjVmNTM3NDNhYmJiZDRhMDY2MDU4OWQ3NDI=|1545380300|de1143c7e1f1120a504f428ca6116925737fcec7",
    'tgw_l7_route':'5bcc9ffea0388b69e77c21c0b42555fe',
    'tst':'r',
    'z_c0':"2|1:0|10:1545380393|4:z_c0|92:Mi4xTi1XbkF3QUFBQUFBb0tBaEIwcXhEaVlBQUFCZ0FsVk5LZkFKWFFCV1dpeE5wWHhOaE9oTHJHUXoya2lrbWcwc29R|dcd28ab9281df3ba586ebfe85ce341a68b7150c555387872d87440e04f90d7a1"
}
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Host':'www.zhihu.com',
    'Connection':'keep-alive'
}
check = {
    'include':'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics',
    'offset':'',	
    'limit':str(3),
    'sort_by':'default',
    'platform':'desktop'
}
link_list = []
main_answer = []
def main():
    link = 'https://www.zhihu.com/'
    r = requests.get(link,headers=headers,cookies=cookie1)
    soup = BeautifulSoup(r.text,'html.parser')
    title = soup.select('h2.ContentItem-title a')
    print('第1次爬取结果：')
    for each in title:
        print(each.text)
    print('---------------------------')
    script = soup.select_one('script#js-initialData')
    taoken = re.compile('session_token=.+?\"')
    result = taoken.findall(script.text)
    #print(result[0].replace('"',''))
    next_link = 'https://www.zhihu.com/api/v3/feed/topstory/recommend?'+result[0].replace('"','')
    for i in range(1,2):
        next_link = get_title(next_link,i+1)   


def get_title(next,number):
    r = requests.get(next,headers=headers,cookies=cookie1)
    js = json.loads(r.text)
    data = js['data']
    try:
        print('第'+str(number)+'次爬取结果：')
        for each in data:
            title = each['target']['question']['title']
            id = each['target']['id']
            id2 = each['target']['question']['id']
            print(title)
            answer_link = 'https://www.zhihu.com/question/'+str(id2)+'/answer/'+str(id)
            more_answer_link = 'https://www.zhihu.com/api/v4/questions/'+str(id2)+'/answers?'
            link_list.append(more_answer_link) #用来爬每个问题下的更多回答
            main_answer.append(answer_link) # 用来爬每个问题下的第一个回答
            '''with open('D://zhihu_new.csv','a+',encoding='UTF-8',newline='') as csvfile:
                w = csv.writer(csvfile)
                w.writerow([title,question_link])'''
        print('-----------------------------')
    except KeyError:
        print('发生了一个错误...')
    finally:
        if not js['paging']['is_end']:
            next_link = js['paging']['next']
            return next_link
        else:
            print('已到最后一页')
            exit()
def get_main_answer():
    '''for each in main_answer:
        r = requests.get(each,cookies=cookie1)
        soup = BeautifulSoup(r.text,'html.parser')

        content = soup.select('div.RichContent RichContent--unescapable div.RichContent-inner span.RichText ztext CopyrightRichText-richText')
        print(content)'''
    print(main_answer[0])
    r = requests.get(main_answer[0],headers=headers,cookies=cookie1)
    soup = BeautifulSoup(r.text,'html.parser')
    title = soup.find('h1',class_='QuestionHeader-title')
    content = soup.find('div',class_='RichContent-inner')
    content = content.span.text
    title = title.text
    print(title)
    print(content)

main()
get_main_answer()
