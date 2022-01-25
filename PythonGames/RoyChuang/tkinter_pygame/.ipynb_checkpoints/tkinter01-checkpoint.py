#%% Import Tkinter

from tkinter import *
get_ipython().run_line_magic('gui', 'tk')

# tk = Tk()
# %% tk = Tk()
tk = Tk()

#%% Button
def create_button():

    def click():
        print("click")


    button = Button(tk, text="Click Me", command=click)
    button.pack()

#%% Canvas
def create_canvas():
    global canvas
    canvas = Canvas(tk,width = 500,height = 500)
    canvas.pack()
    
def draw_line():
    canvas.create_line(0,0,500,500)

def draw_rectangle():
    x1 = 10
    y1 = 10
    x2 = 50
    y2 = 50
    canvas.create_rectangle(x1,x2,y1,y2)

#%% main

# create_button()
create_canvas()
draw_line()
draw_rectangle()
tk.mainloop()

#%%
