from time import sleep,ctime
import threading
def super_player(file_name):
    for i in range(2):
        print('Start Playing: %s! %s' %(file_name,ctime()))
        sleep(1)
list_file = ['爱情买卖','阿凡达','我和你']
files = range(len(list_file))
# 创建线程
threads = []
for file_name in files:
    t = threading.Thread(target=super_player,args=(list_file[file_name],))
    threads.append(t)
if __name__ == '__main__':
    #启动线程
    for i in files:
        threads[i].start()
for i in files:
    threads[i].join()
    # 主线程
    print('end:%s' %(ctime()))
