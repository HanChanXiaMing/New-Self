#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

class Application(Frame):
  def __init__(self, master=None)
    Frame.__init__(self, master)
    # pack()方法把Widget加入到父容器中，并实现布局
    self.pack()
    self.createWidgets()
    
   def createWidgets(self):
    self.helloLabel = Label(self, text = 'Hello, world!')
    self.helloLabel.pack()

    self.quitButton = Button(self, text = 'Quit', command = self.quit)
    self.quitBUtton.pack()
    
app = Application()
# 设置窗口标题:
app.mastr.title('Hello, World')
# 主消息循环:
app.mainlop()
