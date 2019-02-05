import requests,json,re,csv,os,shutil
from bs4 import BeautifulSoup
from urllib.request import quote
import urllib
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
headers = {# 搜索页请求头
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Host':'www.zhihu.com',
    'Referer':'https://www.zhihu.com/',
    'Connection':'keep-alive',
    'Accept-Language':'zh-CN,zh;q=0.8'
}
check = {
    'include':'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics',
    'offset':'',	
    'limit':str(3),
    'sort_by':'default',
    'platform':'desktop'
}
def main(): # 首页
    '''del_file('D:\\azhihu_picture\\')
    dir_list = os.listdir('D:\\azhihu_picture\\')
    for dir_name in dir_list:
        Null_dir_path = 'D:\\azhihu_picture\\'+dir_name
        shutil.rmtree(Null_dir_path)'''
    a = input('输入搜索关键词：')
    a = a.encode('UTF-8')
    link = 'https://www.zhihu.com/search?type=content&q='+quote(a)
    r = requests.get(link,headers=headers,cookies=cookie1,timeout=10)
    soup = BeautifulSoup(r.text,'html.parser')
    ti = soup.find_all('div',class_='Card SearchResult-Card') #定位该关键词下的前5个问题
    script = soup.select_one('script#js-initialData') #定位该关键词下的第二个“5个问题”
    n = re.compile('\d+') #正则--匹配数字
    global number
    for each in ti:
        #print(each)
        try:
            #title = each.select('span.Highlight')[0] # 首页里的问题
            #title_name = title.text
            link = each.select('h2.ContentItem-title meta')[0] 
            answer_link = link.get('content')  #获取该回答的网址
            number = n.findall(answer_link)[0]  #取得链接里面的问题编号
            get_answer(answer_link)
        except IndexError:
            pass                                                                                                                                                                                          
    question_number = re.compile('question":{"id":"(\d+)"')
    question_numbers = question_number.findall(script.text) #获得第二个“5个问题”里的回答
    for each in question_numbers: # 列表里为全数字
        #print('正在获得'+title_name+' 第二个"5个问题"')                                                                                                                                                                        
        each_fivth_answer = 'https://www.zhihu.com/question/'+str(each) 
        # 获得第二个 “5个问题”
        number = n.findall(each_fivth_answer)[0]
        get_answer(each_fivth_answer) #获得第二个 “5个问题”的所有回答
    print('---------------------------') 

        

def get_answer(link):
    r = requests.get(link,headers=headers,cookies=cookie1,timeout=10)
    soup = BeautifulSoup(r.text,'html.parser')
    answer = soup.find_all('div',class_='ContentItem AnswerItem') #定位链接里所有回答
    script = soup.select_one('script#js-initialData') #定位该关键词下的第二个“5个回答”    
    global title_name 
    title_name = soup.find('h1',class_='QuestionHeader-title')
    title_name = title_name.text
    print('-------------')
    print('正在下载"'+title_name+'"的图片'+'\n编号为'+number)  
    print('-------------')
    try:
        path = 'D:\\azhihu_picture\\'+title_name 
        os.makedirs(path)  #创建对应的问题名的目录
    except FileExistsError:
        print('该回答里的图片已经爬取，已跳过') 
    print('正在下载"'+title_name+'"的图片')    
    for each in answer: #获取前两个回答的图片
        content = each.find('span',class_='RichText ztext CopyrightRichText-richText') #定位回答内容
        jpg = content.find_all('img',class_='origin_image zh-lightbox-thumb lazy') #定位回答内容里的图片
        imgname = 1
        for each2 in jpg:
            downlink = each2.get('data-original')  #获取图片链接
            urllib.request.urlretrieve(downlink,path+'\\'+str(imgname)+'.jpg') #下载图片
            imgname += 1
        print('-----------------')
    # 获取 script里面的回答内容
    jpg_re = re.compile('data-original="(.*?)"')
    jpg_links1 = jpg_re.findall(script.text)
    jpg_links = list(set(jpg_links1))
    jpg_links.sort(key=jpg_links1.index)
    for i in jpg_links:
        urllib.request.urlretrieve(i,path+'\\'+str(img_name)+'.jpg') #下载图片
        img_name += 1
    #  该问题下的回答的下一页的链接
    link = 'https://www.zhihu.com/api/v4/questions/'+number+'/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=15&platform=desktop&sort_by=default'
    next_page(link,number,imgname,path)
    
def next_page(link_,num_,img_name,path_):
    print('问题'+num_+'继续爬取中...')

    data1 = {
        'include':'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics',        'limit':'5',
        'offset':'15',
        'platform':'desktop',
        'sort_by':'default'
    }
    headers2 = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Host':'www.zhihu.com',
        'Referer':'https://www.zhihu.com/question/'+num_,
        'Connection':'keep-alive',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'origin':'https://www.zhihu.com',
        'TE':'Trailers',
        'x-udid':'AKCgIQdKsQ6PTm7RQYWtvtdkh-t274iFX6w=',
        'x-requested-with':'fetch',
        'Accept':'*/*',
        'Accept-Encoding':'UTF-8'
            }
    try:
        r = requests.get(link_,headers=headers2,data=data1,cookies=cookie1,timeout=10)
        js = json.loads(r.text)
        data = js['data']
        jpg = re.compile('data-original="(.*?)"') #正则表达式，匹配 图片链接
        for each in data:
            a = each['content']  #获取回答内容
            a = jpg.findall(a)   #过滤出图片链接
            a1=list(set(a))
            a1.sort(key=a.index) #去除重复的图片链接
            for i in a1:
                urllib.request.urlretrieve(i,path_+'\\'+str(img_name)+'.jpg') #下载图片
                img_name += 1
        if not js['paging']['is_end']: #如果没有到最后一页，就继续
            #a = input('是否下一页')
            next_link = js['paging']['next']  #获取下一页的链接
            next_page(next_link,num_,img_name,path_)  #递归
        else:
            print('该问题已爬取完毕')
    except requests.exceptions.ChunkedEncodingError:
        print('编码失败，跳过该问题')  
def del_file(path):  # 删除目录函数，不用每次手动删除图片
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)
main()  # 运行主函数