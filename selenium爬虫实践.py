from selenium import webdriver
import random
import time
import re
import pyodbc
import csv
from selenium.common.exceptions import NoSuchElementException
# 房子所有数据地址 div._v72lrv  
# 价格数据 span._1sfeueqe
# 评价星级 span._q27mtmr
# 房屋名称 div._190019zr
# 评价数量 span._1m8bb6v
# star = eachhouse.find_elements_by_css_selector('span._q27mtmr>span>span._z1pr8k6')
# stars = len(star) --- 这两句获取星级

#conn = pyodbc.connect('driver=SQL Server Native Client 10.0;server=ALEX_HUA;database=house;uid=sa;pwd=787001245')
#cursor = conn.cursor()  --->调用数据库 与 获取游标

driver = webdriver.Firefox()
pages = 10
link = r'https://zh.airbnb.com/s/Guangzhou--China/homes?refinement_paths%5B%5D=%2Fhomes&click_referer=t%3ASEE_ALL%7Csid%3A85ed8222-791b-47b1-bf70-8868818afef4%7Cst%3AMAGAZINE_HOMES&superhost=true&query=Guangzhou%2C%20China&title_type=MAGAZINE_HOMES&allow_override%5B%5D=&s_tag=aR3YJngb'

for page in range(1,pages+1):
    if page == 0:
        driver.get(link)
    else:
        link_true = link+'&section_offset=6&items_offset='+str(page*18)
        driver.get(link_true)
    sleep_seconds = random.uniform(1,2)
    house_list = []
    rent_list = driver.find_elements_by_css_selector('div._v72lrv')
    for eachhouse in rent_list:
        try:
            name = eachhouse.find_element_by_css_selector('div._190019zr') 
            name = name.text
            price = eachhouse.find_element_by_css_selector('span._1sfeueqe')
            price = price.text
            p = re.compile(r'[\d]+')
            price = p.findall(price)[0]
            comment = eachhouse.find_element_by_css_selector('span._1cy09umr')
            comment = comment.text
            star = eachhouse.find_elements_by_css_selector('span._q27mtmr>span>span._z1pr8k6')
            stars = len(star)
            eachhouse_data = {'房源':name,'价格':price+'元','星级':stars,'评论数量':comment}
            house_list.append(eachhouse_data)
            with open('D://text101.csv','a+',encoding='UTF-8',newline='') as csvfile:
                w = csv.writer(csvfile)
                w.writerow([name,price,str(stars),comment])
            time.sleep(sleep_seconds)
        except NoSuchElementException as msg:
            print("第"+page+"页出现错误：没有定位到元素:"+msg)
driver.close()


'''string = "insert house_data values("+name+","+price+","+str(stars)+","+comment+")"
cursor.execute(string)
conn.commit()#
cursor.execute(sql)   %传递sql语句给数据库
conn.close()'''