from tkinter import *
import win32api
import win32con
from sun_movie import *
from movie_haven_Gui import *
from tkinter import scrolledtext
main_link = 'https://www.dy2018.com/e/search/index.php'
class Moive_Spider(object):
    def __init__(self):
        self.root = Tk()
        self.createpage()
    def createpage(self):
        self.root.title("Movie Spider")
        self.root.geometry('800x400+400+200')
        frame_root = Frame(self.root)
        frame_root.pack()
        frame_1 = Frame(frame_root)
        frame_2 = Frame(frame_root)
        frame_3 = Frame(frame_root)
        label1 = Label(frame_1,text='请输入要查找的电影名',font=('宋体',14),width=18,height=2)
        label1.pack()
        movie_name = StringVar()
        enter = Entry(frame_1,highlightthickness=1,highlightcolor='red',textvariable=movie_name)
        enter.pack()
        var = IntVar()
        var.set(1)
        b1 = Radiobutton(frame_2,font=('宋体',14),text='电影天堂',variable=var,value=1)
        b1.pack(side=LEFT)
        kongge = Label(frame_2,text='  ')
        kongge.pack(side=LEFT)
        check = Button(frame_3,text='搜索')
        label4 = Label(frame_3,text='----------------------------------------------------------------')
        label4.pack()
        #check.bind("<Button-1>", check)
        check.pack()
        t1 = scrolledtext.ScrolledText(frame_3,width=200,height=20)
        t1.pack()
        frame_1.pack(side=TOP)
        frame_2.pack(side=TOP)
        frame_3.pack(side=BOTTOM)
        #download = b1.bind('<Button-1>',yangguang('蜘蛛侠'))
        b1['command'] = lambda:Moive_Spider.a(self)
        check['command'] = lambda:(movie_haven(main_link,enter.get().encode('gbk'),t1))
        self.root.mainloop()
    def a(self):
        print('1')


start = Moive_Spider()
