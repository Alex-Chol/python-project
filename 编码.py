from urllib.request import quote
import  urllib.parse

a = '长腿'.encode('UTF-8')
a = '%5B%2A%5D'
a = urllib.parse.unquote(a)
print(a)
# %D6%A9%D6%EB%CF%C0
# https://www.zhihu.com/search?type=content&q=%E9%95%BF%E8%85%BF
