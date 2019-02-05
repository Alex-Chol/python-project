from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re
#driver = webdriver.Chrome()
caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = True
driver = webdriver.Firefox()
driver.get('http://www.santostang.com/2018/07/04/hello-world/')
#print(driver.page_source) -->返回网页源代码
#       XXX.get_attribute('innerHTML')返回某个元素的源代码
#name = driver.find_elements_by_css_selector('div')

#print(name)
#name2 = name.find_element_by_css_selector('div.slide-page')
#for i in name:
#    print(i.read())

'''re1 = r'[\D]+'
com = re.compile(re1)
for i in name:
    print(com.findall(i.text.strip()))'''

driver.close()