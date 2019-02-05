from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
fp = webdriver.FirefoxProfile()
fp.set_preference("permisssion.default.stylesheet",2)
caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = True
driver = webdriver.Firefox(firefox_profile=fp,capabilities=caps)
driver.get("http://www.santostang.com/2018/07/04/hello-world/")
driver.close()