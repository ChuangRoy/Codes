# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:33:42 2020

@author: Roy

copy_by:https://www.itread01.com/content/1545909497.html

"""

from tkinter import *
import random

showAnswer = True

def ReStart():
    global GameNumber
    GameNumber = random.randrange(1, 100)
    if showAnswer == True:
        print(GameNumber)

ReStart()

root = Tk()
root.title("GuessNumber")

num = StringVar()
E1 = Entry(root,width = 5,textvariable = num,font=("", 40))
b = num.set('')

var = StringVar()
label = Label( root, textvariable=var,bg = 'red',width = 50,font=("", 20))
var.set("從1-100中隨機選擇一個數字，請你猜測這個數字是多少？")

def EnterClick(event):
    a = E1.get()
    isNum = a.isdigit()
    print(isNum)
    if isNum:
        number = int(a)
        if number > GameNumber:
            var.set("請輸入小一點的數字" )
            b = num.set('')
        elif number < GameNumber:
            var.set("請輸入大一點的數字" )
            b = num.set('')
        else:
            var.set("恭喜你，猜對了!是否繼續遊戲？(Y/N)")
            b = num.set('')
    else:
        if a == 'y' or a == 'Y':
            ReStart()
            b = num.set('')
            var.set("從1-100中隨機選擇一個數字，請你猜測這個數字是多少？")
        elif a== 'n' or a =='N':
            root.destroy()
            b = num.set('')
        else:
            b = num.set('')

def onclick():
    a = E1.get()
    isNum = a.isdigit()
    print(isNum)
    if isNum:
        number = int(a)
        if number > GameNumber:
            var.set("請輸入小一點的數字")
            b = num.set('')
        elif number < GameNumber:
            var.set("請輸入大一點的數字")
            b = num.set('')
        else:
            var.set("恭喜你，猜對了!是否繼續遊戲？(Y/N)")
            b = num.set('')
    else:
        if a == 'y' or a == 'Y':
            ReStart()
            b = num.set('')
            var.set("從1-100中隨機選擇一個數字，請你猜測這個數字是多少？")
        elif a== 'n' or a =='N':
            root.destroy()
            b = num.set('')
        else:
            b = num.set('')

button = Button(root,text = "輸入",font=("", 25),command =lambda:onclick())

E1.bind('<Return>',EnterClick)
button.pack(side = BOTTOM)

E1.pack(side = BOTTOM)
label.pack()
root.mainloop()
