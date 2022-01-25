import threading

lock = threading.Lock()
def sub():
    global var
    #---------------↓ 鎖定區域 A ↓---------------#
    lock.acquire()  # 進行鎖定
    print('sub (befor):', var)
    var -= 1
    print('sub (after):', var)
    print('--------')
    lock.release()  # 釋放鎖定
    #---------------↑ 鎖定區域 A ↑---------------#
def add():
    global var
    #---------------↓ 鎖定區域 B ↓---------------#
    lock.acquire()
    var += 20
    lock.release()
    #---------------↑ 鎖定區域 B ↑---------------#
var = 10
for i in range(30):
    a = threading.Thread(target = sub).start()
    b = threading.Thread(target = add).start()