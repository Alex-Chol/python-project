import re,threading,requests
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
}
def get_status(url):
    try:
        response = requests.get(url,headers=header,timeout=10)
        print(url+'\t'+str(response.status_code))
    except requests.exceptions.ConnectionError:
        print('这个网站出错啦！  错误类型：1')
    except UnboundLocalError:
        print('这个网站出错啦！  错误类型：2')
    except requests.exceptions.ReadTimeout:
        print('这个网站超时啦！')
f = open(r"C:\Users\Shinelon\Documents\我的文档\Python\Robots\alexa.txt",'r')
link = f.read()
f.close()
re = re.compile('(https*://www\..+)\n')
links = re.findall(link)
threads = []
for each in links:
    t = threading.Thread(target=get_status,args=(each,))
    threads.append(t)
for i in range(len(threads)):
    threads[i].start()
for i in range(len(threads)):
    threads[i].join()

