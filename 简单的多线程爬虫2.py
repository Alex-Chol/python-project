import threading
import requests
import time
link_list = []
with open('alexa.txt','r') as file1:  
    file_list = file1.readlines()
    for eachone in file_list:
        link = eachone.split('/t')[1] #分割序号与网址
        link = link.replace('\n',' ')  #用空格代替\n
        link_list.append(link)
start = time.time()
class myThread (threading.Thread):
    def __init__(self,name,link_range):
        threading.Thread.__init__(self)
        self.name = name 
        self.link_range = link_range
    def run(self):
        print("Starting " + self.name)
        crawler(self.name,self.link_range)
        print("Exiting "+self.name)
def crawler(threadName,link_range):
    for i in range(link_range[0],link_range[1]+1):
        try:
            r = requests.get(link_list[i],timeout = 20)
            print(threadName,r.status_code,link_list[i])
            except Exception as e:
                print(threadName,'Error: ',e)
thread_list = []
link_range_list = [(0,200),]