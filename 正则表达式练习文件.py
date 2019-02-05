import re
key = r"feaeurl: https://movie.douban.com/subject/26366496/jidojhttp://movie.douban.com/subject/26985127/feasfehttps://movie.douban.com/subject/27605698/"

a = re.compile(r"https*://[^/]+/[^/]+/[\d]+/")
#a = re.compile(r"https*://[^/]+/")

print(a.findall(key))