import  requests

header = {# 搜索页请求头
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
data = {
'tn':'baiduimage',
'ipn':'r',
'ct':'201326592',
'cl':'2',
'lm':'-1',
'st':'-1',
'fm':'result',
'fr':''	,
'sf':'1',
'fmq':'1546095953666_R',
'pv':''	,
'ic':'0',
'nc':'1',
'z':'0',
'hd':'0',
'latest':'0',
'copyright':'0',
'se':'1',
'showtab':'0',
'fb':'0',
'width':'',
'height':''	,
'face':'0',
'istype':'2',
'ie':'utf-8',
'ctd':'1546095953667^00_1097X909',
'word':'壁纸+',
}
re = requests.get('http://image.baidu.com/search/index',headers=header,data=data)
