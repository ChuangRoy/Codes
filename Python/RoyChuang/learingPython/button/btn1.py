from tkinter import*
tk = Tk()
def hello():
    print('hello world')
btn = Button(tk,text = "chick me",command=hello)
btn.pack()
