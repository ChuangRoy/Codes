import threading

def sub():
    global var
    print('sub (befor):', var)
    var -= 1
    print('sub (after):', var)
    print('--------')
def add():
    global var
    var += 20

var = 10
for i in range(30):
    a = threading.Thread(target = sub).start()
    b = threading.Thread(target = add).start()