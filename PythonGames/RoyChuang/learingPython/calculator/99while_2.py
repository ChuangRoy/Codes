your_number = [9,9]
num1 = 1
num2 = 1
while num1 < your_number[0]+1:
    while num2 < your_number[1]+1:        
        print("%d * %d = %d " % (num1,num2, num1*num2))
        num2 = num2 + 1
    num1 = num1 + 1
    num2 = 1

        
