import subprocess as sp       # 更名為 sp
						            # 嚴重警告！請勿建立子行程來執行自己 (8-19.py),
print('Main Process start')	#↓  否則會陷入無窮自我呼叫, 造成當機。
p = sp.Popen('python 8-18.py',
             shell=True,
             stdout= sp.PIPE, stderr= sp.PIPE)
result = p.communicate()	# 取得結果
print('Returncode:', p.returncode) #← ReturnCode 為 0 代表子行程執行正確, 其他(例如 1) 為發生錯誤的錯誤代碼
print('標準結果輸出：', result[0])
print('標準錯誤輸出：', result[1])
print('Main Process Finish')	 	# 要等子行程結束才印出
