import requests
from bs4 import BeautifulSoup
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
r = requests.get('http://qstv3.com/forum.php?mod=forumdisplay&fid=128',headers=header)
soup = BeautifulSoup(r.text,'html.parser')
print(soup.text)