import requests
import time
import json
text = input('请输入一个词语,不少于30个字符：\n')
print('分析中...')
while len(text) < 30:
    print('错误！')
    text = input('请输入30个以上的字符：\n')
dict1 = {'content':text,'type':'all'}
link = r'http://ictclas.nlpir.org/nlpir/index/getAllContentNew.do'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'}
r = requests.post(link,data=dict1,headers=headers)
dictword = json.loads(r.text)['dividewords']
dictword = dictword.split(' ')
text2 = []
mean = [] 
for each in dictword:
    if each == dictword[-1]:
        continue            #少了这一步无法运行，因为dictord最后一项是空的，split后只有一个元素
    else:                   # 也就不存在list1[1]
        list1 = each.split('/')
        text2.append(list1[0])
        mean.append(list1[1])
time.sleep(1)
print('/'.join(text2))
print('每个词语对应的词义为:\n'+'/'.join(mean))
