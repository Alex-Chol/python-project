import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
r = requests.get('https://www.ele.me/place/ws0eqm8bet27?latitude=23.101616&longitude=113.478964')
#r = requests.get('http://www.baidu.com/')
print('文本编码：', r.encoding)
print('响应文本码：', r.status_code)
print('字符串方式的响应体：', r.text)
