from tkinter import*
import turtle
t = turtle.Pen()
tk = Tk()
def forward():
    t.forward(10)
def backward():
    t.backward(10)
def left():
    t.left(10)
def right():
    t.right(10)
def up():
    t.up()
def down():
    t.down()
def stfill():
    t.begin_fill()

Button(tk,text = 'forward',command=forward).pack()
Button(tk,text = 'backward',command=backward).pack()
Button(tk,text = 'left',command=left).pack()
Button(tk,text = 'backward',command=backward).pack()
Button(tk,text = 'backward',command=backward).pack()