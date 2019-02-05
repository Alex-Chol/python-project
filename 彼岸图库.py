# http://pic.netbian.com/downpic.php?id=9185&classid=53  下载图片的请求网址
import requests,threading,random,time
from bs4 import BeautifulSoup
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Host':'pic.netbian.com',
    'Referer':'http://pic.netbian.com/tupian/9185.html'
}
data = {
    '__cfduid':'dafee21ed5593eb0289078be8db33d4191546096732',
    'ctrl_time':'1',
    'Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e':'1548089750',
    'Hm_lvt_14b14198b6e26157b7eba06b390ab763':'1546096736,1548073782',
    'Hm_lvt_526caf4e20c21f06a4e9209712d6a20e':'1546096752,1548073791,1548087088',
'PHPSESSID':'8b5295b368239ae7d07e023617ef9eac',
'security_session_verify':'dfe4064483fc22a2e1079ca4791a5a04',
'yjs_id':'e301afb619eb84d5bc466eaeb8312050',
'zkhanecookieclassrecord':' ,53,54',
'zkhanmlauth':'f3452565c39f20f16d5ec803808e05a0',
'zkhanmlgroupid':'1',
'zkhanmlrnd':'S5wmR6r0IjH4FpG8PwHI',
'zkhanmluserid':'974659',                            
}
url = 'http://pic.netbian.com/4kmeinv/'
number = 1
def get_photo(url):
    try:
        r = requests.get(url,headers=header,cookies=data,timeout=10)
    except:
        print('出错啦！')
    r = r.content.decode('gbk','ignore')
    soup = BeautifulSoup(r,'html.parser')
    jpg = soup.select('ul.clearfix li a img')
    global number
    for each in jpg:
        link = each.get('src')
        link = 'http://pic.netbian.com'+link
        get_jpg = requests.get(link)
        #print(link+'\n-------------------')
        jpg = open('D:\\123\\biantuku\\'+str(number)+'.jpg','wb')
        number += 1
        jpg.write(get_jpg.content)
        jpg.close()
    time.sleep(random.uniform(1,3))

# http://pic.netbian.com/uploads/allimg/180514/155349-1526284429d06e.jpg
# http://pic.netbian.com/4kmeinv/index_4.html  总共192页
get_photo(url)
threads = []
next_urls = []
page = 2
for i in range(191):
    next_url = 'http://pic.netbian.com/4kmeinv/index_'+str(page)+'.html'
    next_urls.append(next_url)
    page += 1
# 全部网址已经装好入列表
for each in range(len(next_urls)): #将运行的函数装入线程
    t = threading.Thread(target=get_photo,args=(next_urls[each],))
    threads.append(t)
if __name__ == '__main__':
    for i in range(191):
        threads[i].start()
for i in range(191):
    threads[i].join()
