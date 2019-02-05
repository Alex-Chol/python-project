from tkinter import *
import win32api
import win32con
from sun_movie import *
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
        label2 = Label(frame_2,text='请选择搜索源，默认为阳光电影')
        label2.pack()
        var = IntVar()
        var.set(1)
        b1 = Radiobutton(frame_2,font=('宋体',14),text='阳光电影',variable=var,value=1)
        b2 = Radiobutton(frame_2,font=('宋体',14),text='电影天堂',variable=var,value=2)
        b1.pack(side=LEFT)
        kongge = Label(frame_2,text='  ')
        kongge.pack(side=LEFT)
        b2.pack(side=RIGHT)
        check = Button(frame_3,text='搜索')
        label4 = Label(frame_3,text='----------------------------------------------------------------')
        label4.pack()
        #check.bind("<Button-1>", check)
        check.pack()
        t1 = Text(frame_3,width=200,height=20)
        t1.pack()
        frame_1.pack(side=TOP)
        frame_2.pack(side=TOP)
        frame_3.pack(side=BOTTOM)
        #download = b1.bind('<Button-1>',yangguang('蜘蛛侠'))

        b1['command'] = lambda:Moive_Spider.a(self)
        b2['command'] = lambda:Moive_Spider.b(self)
        
        check['command'] = lambda:(yangguang(enter.get(),t1))
        self.root.mainloop()
    def a(self):
        print('1')
    def b(self):
        print('2')

start = Moive_Spider()
