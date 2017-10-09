#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import fq

from Tkinter import *
root = Tk()

root.title('fq_py_supermans1201')
root.geometry('200x100')
root.iconbitmap(os.path.join(fq.getpath(),u"fq.ico"))

strvar = StringVar()
strvar0=StringVar()
strvar1=StringVar()
strvar.set(u"使用翻墙host")  # 要改要成的文本


def handler():
    fq.fqYes()

btn = Button(root, textvariable=strvar, command=handler) #textvariable设置原文本，command=handler是设置按钮要执行的代码
btn.pack()

def openhosthandler():
    fq.openHost()
openhoststrvar = StringVar()
openhoststrvar.set(u"打开host文件")
openhostbtn = Button(root,textvariable=openhoststrvar, command=openhosthandler)
openhostbtn.pack()

def resethosthandler():
    fq.fqNo()

resethoststrvar = StringVar()
resethoststrvar.set(u"重置host文件")
resethostbtn = Button(root,textvariable=resethoststrvar, command=resethosthandler)
resethostbtn.pack()
# 进入消息循环
root.mainloop()