def move(n,a,b,c):
    global i
    if n == 1:
        i += 1
        print(i,a,"->",c)
        file.write(f"{i}{a}->{c}\n")
       
    else:
        move(n-1,a,b,c)
        i += 1
        print(i,a ,"->" ,b)
        file.write(f"{i}{a}->{b}\n")
        move(n-1,c,b,a)
        i += 1
        print(i,b,"->",a)
        file.write(f"{i}{b}->{a}\n")
        move(n-1,a,b,c)
    
     

i = 0
hanoi = \
"""""
   [||]     ||      ||
  [ || ]    ||      ||
 [  ||  ]   ||      ||

================================

    a       b        c
"""""
import os
import time
print(hanoi)
steps = input("請問要移動幾階漢諾塔：")
steps = int(steps)
print()
print(steps,"階漢諾塔移動步驟")
file = open("hanoi.txt","a")
file.write(f"{steps}階漢諾塔移動步驟\n")
start = time.time()
move(steps,"a","b","c")
print(time.time()-start)
os.system("pause")
