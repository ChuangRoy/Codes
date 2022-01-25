'''

copy_by:https://www.itread01.com/content/1546288575.html

'''

from tkinter import *  
import tkinter.simpledialog as dl  
import tkinter.messagebox as mb    

root = Tk()   
w = Label(root, text = "Guess Number Game") 
w.pack()      

mb.showinfo("yunyaniu", "Welcome to Guess Number Game")  

number = 2018
while True:
    guess = dl.askinteger("yunyaniu", "What's your guess?") 
    if guess == number:
        # New block starts here
        output = 'Bingo! you guessed it right, but you do not win any prizes!'
        mb.showinfo("Hint: ", output)
        break
        # New block ends here
    elif guess < number:
        output = 'No, the number is a  higer than that'
        mb.showinfo("Hint: ", output)
    else:
        output = 'No, the number is a  lower than that'
        mb.showinfo("Hint: ", output)
mb.showinfo("yunyaniu","Thank you for your participation！") 
print('Game over!')  