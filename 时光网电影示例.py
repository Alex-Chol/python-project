import requests
import re
import time
import json
from bs4 import BeautifulSoup as BS
import sys
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
}
 
def Get_Movie_URL():
	urls = []
	for i in range(1,11):
		# 第一页的URL是不一样的，需要另外进行处理
		if i != 1:
			url = "http://www.mtime.com/top/movie/top100/index-%d.html" % i
		else:
			url = "http://www.mtime.com/top/movie/top100/"
		r = requests.get(url=url,headers=headers)
		soup = BS(r.text,'lxml')
		movies = soup.find_all(name='a',attrs={'target':'_blank','href':re.compile('http://movie.mtime.com/(\d+)/'),'class':not None})
		for m in movies:
			urls.append(m.get('href'))
	return urls
 
def Create_Ajax_URL(url):
	movie_id = url.split('/')[-2]
	t = time.strftime("%Y%m%d%H%M%S0368", time.localtime())
	ajax_url = "http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_RequestUrl=%s&t=%s&Ajax_CallBackArgument0=%s" % (url,t,movie_id)
	return ajax_url
 
def Crawl(ajax_url):
	r = requests.get(url=ajax_url,headers=headers)
	if r.status_code == 200:
		r.encoding = 'utf-8'
		result = re.findall(r'=(.*?);',r.text)[0]
		if result is not None:
			value = json.loads(result)
 
			movieTitle = value.get('value').get('movieTitle')
			TopListName = value.get('value').get('topList').get('TopListName')
			Ranking = value.get('value').get('topList').get('Ranking')
			movieRating = value.get('value').get('movieRating')
			RatingFinal = movieRating.get('RatingFinal')
			RDirectorFinal = movieRating.get('RDirectorFinal')
			ROtherFinal = movieRating.get('ROtherFinal')
			RPictureFinal = movieRating.get('RPictureFinal')
			RStoryFinal = movieRating.get('RStoryFinal')
			print(movieTitle)
			if value.get('value').get('boxOffice'):
				TotalBoxOffice = value.get('value').get('boxOffice').get('TotalBoxOffice')
				TotalBoxOfficeUnit = value.get('value').get('boxOffice').get('TotalBoxOfficeUnit')
				print('票房：%s%s' % (TotalBoxOffice,TotalBoxOfficeUnit))
			print('%s——No.%s' % (TopListName,Ranking))
			print('综合评分：%s 导演评分：%s 画面评分：%s 故事评分：%s 音乐评分：%s' %(RatingFinal,RDirectorFinal,RPictureFinal,RStoryFinal,ROtherFinal))
			print('****' * 20)
 
def main():
	urls = Get_Movie_URL()
	for u in urls:
		Crawl(Create_Ajax_URL(u))
 
	# 问题所在，请求如下单个电影链接时时不时会爬取不到数据
	# Crawl(Create_Ajax_URL('http://movie.mtime.com/98604/'))
 
if __name__ == '__main__':
	main()