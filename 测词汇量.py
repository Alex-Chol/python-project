import requests,json,time
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Host':'www.shanbay.com',
    'origin':'https://www.shanbay.com',
    'Referer':'https://www.shanbay.com/bdc/client/vocabtest/welcome'
}  #修改请求头
url = 'https://www.shanbay.com/api/v1/vocabtest/category/'  #请求网址
r = requests.get(url,headers=header)  #请求网址响应
js_first = json.loads(r.text)  #将获取到的json文件进行分析
bianhao = int(input('''请输入你选择的词库编号，按Enter确认

1，GMAT  2，考研  3，高考  4，四级  5，六级

6，英专  7，托福  8，GRE  9，雅思  10，任意

''')) #  要求用户输入相应编号
data = js_first['data'][bianhao-1][0]          #获取用户输入的词库代号
subject_name = js_first['data'][bianhao-1][1]  #获取用户输入的词库名称
test_link = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+data  #下一步的链接
r = requests.get(test_link,headers=header)  #请求网址响应
js = json.loads(r.text)  #分析json文件
words = js['data']      #将json文件里的data名称数据赋予words
print('选择你认识的单词，认识的单词请输入 y，不认识的请按回车（Enter）')
time.sleep(1)
know_word = {}      #用户认识的单词存放在此字典
unknow_word = {}    #用户不认识的单词存放在此字典
word_ranks = []     #所有单词的rank值存放在此列表
for number in range(len(words)):    #循环次数为单词数量
    word_ranks.append(words[number]['rank']) #收集所有单词的rank值
    while(True):    #为保证程序的正确运行，若输入错误字符将重新运行本次循环
        user_know = input(words[number]['content']+'  --  ')    #用户输入是否认识
        if user_know == 'y' or user_know == 'Y':    
            pk = words[number]['pk']                                #将认识的单词pk值赋予pk变量
            rank = words[number]['rank']                            #将认识的单词rank值赋予rank变量
            know_word[words[number]['content']] = [number,pk,rank]  #将认识的单词及其相关编号，pk值，rank值存放在字典中
            break   #退出这一个单词的循环，进行下一个单词的认识确认
        elif user_know == '':   #输入了回车
            for each in range(len(words[number]['definition_choices'])):
                if int(words[number]['definition_choices'][each]['rank']) == int(words[number]['rank']):
                    mean = words[number]['definition_choices'][each]['definition']
                    rank = words[number]['definition_choices'][each]['rank']  
                    unknow_word[words[number]['content']] = [number,mean,rank]
                    #将不认识的单词存放在unknow_word字典中  
            break   #退出本次循环
        else:   #如果输入了非Y 或者非回车，即打印错误消息，并重新进行本次循环
            print('输入了无效字符，请重试！')
print('\n接下来我们检测一下你是否真正的掌握了这些单词吧。\n请选择这些单词的意思：')
time.sleep(1)   #为防止误操作，添加一秒的程序延迟
wrong_anwser = {}   #存放回答错误的单词 的字典
right_anwser = []   #存放回答正确的单词 的列表
for word in know_word:  #循环次数为认识的单词数量
    while(True):    #如果输入了非选择项的编号将重新运行本次循环
        print('\n'+word+'的意思是：\n'+'1.'+words[know_word[word][0]]['definition_choices'][0]['definition']+'\n2.'+words[know_word[word][0]]['definition_choices'][1]['definition'])
        print('3.'+words[know_word[word][0]]['definition_choices'][2]['definition']+'\n4.'+words[know_word[word][0]]['definition_choices'][3]['definition'])
        choice = input('选择你的答案：')
        if choice not in ['1','2','3','4']:# 如果用户输入的数据不是[1,2,3,4]中的其中一个
            print('输入有误，请重试！')
        else:    
            answer_rank = words[know_word[word][0]]['definition_choices'][int(choice)-1]['rank'] #获取用户答案的pk值
            if int(answer_rank) == int(know_word[word][2]): #将用户答案的pk与正确答案的pk值比较，如果相等即回答正确
                right_anwser.append(word)
            else:   #回答错误
                for each in range(len(words[know_word[word][0]]['definition_choices'])):
                    if int(words[know_word[word][0]]['definition_choices'][each]['rank']) == int(know_word[word][2]):
                        mean = words[know_word[word][0]]['definition_choices'][each]['definition']
                        wrong_anwser_rank = words[know_word[word][0]]['definition_choices'][each]['rank']
                        wrong_anwser[word] = [know_word[word][0],mean,wrong_anwser_rank]
            break
print('\n\n现在，到了公布成绩的时刻：')
time.sleep(0.5)
#以下是要向服务器post的数据处理
string_word_ranks = ','.join(str(i) for i in word_ranks)    #将word_ranks列表里的元素转换成字符类型再用逗号分隔换成字符串
right_ranks = []    #定义一个right_ranks列表，存放回答正确的单词的rank值
for each in right_anwser:
    right_ranks.append(know_word[each][2])  #将回答正确的单词的rank值放入right_ranks列表
string_right_ranks = ','.join(str(j) for j in right_ranks) #将right_ranks列表里的元素转换成字符类型再用逗号分隔换成字符串
post_data = {
    'category':data,
    'phase':'',
    'right_ranks':string_right_ranks,
    'word_ranks':string_word_ranks
}
p = requests.post('https://www.shanbay.com/api/v1/vocabtest/vocabularies/',headers=header,data=post_data)
post_json = json.loads(p.text)
print('--------------------------------------------------------------------------------\n\t\t你的词汇量大约是'+str(post_json['data']['vocab'])+'''
\t'''+post_json['data']['comment']+'\n--------------------------------------------------------------------------------')
print('在'+str(len(words))+'个'+subject_name+'词汇中，你认识其中'+str(len(know_word))+'个,实际掌握'+str(len(right_anwser))+'个,错误'+str(len(wrong_anwser))+'个')
#生成报告
time.sleep(1)
save = input('是否打印并保存你的错词集？需要就填入Y（大小写皆可），不需要则填入任意键：') #询问用户是否保存错词集
if save == 'Y' or save == 'y': #如果用户说是
    f = open('D:\\错题集.txt','a+') #在当前目录下，创建一个错题集.txt的文档
    print('\n你记错的单词有：\n'+'\t'.join(wrong_anwser.keys()))
    a = 0 
    f.write('你记错的单词有：\n')   #需要添加错题的翻译
    #写入你记错的单词信息
    for each in wrong_anwser:
        a += 1

        f.write(str(a)+'.'+each+'\n释义为：'+wrong_anwser[each][1]+'\n')

    time.sleep(1)
    print('\n你不认识的单词有：\n'+'\t'.join(unknow_word.keys()))
    a = 0
    f.write('你不认识的单词有：\n') #需要添加错词的翻译
    #写入你不认识的单词信息
    for each in unknow_word.keys():
        a += 1
        f.write(str(a)+'.'+each+'\n释义为：'+unknow_word[each][1]+'\n')
    time.sleep(1)
    print('\n错词和没记住的词已经保存至当前文件夹中。下次见！')
    f.close()
else:
    print('下次见！')
    



    

