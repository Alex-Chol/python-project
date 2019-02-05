import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'Host':'www.baidu.com'}
r = requests.get('http://www.baidu.com/',headers=headers)
print('响应状态码：',r.status_code)