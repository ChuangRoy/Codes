# 1
print("\n 1. \n")
a = 100
b = 2000
c, d = a, b
print(c, d)
print()

# 2
print("\n 2. \n")
a = 100
b = 200
c, d = a, b
print(c, d)
print(c, end='')
print(d, end='***')
print("Over")

# 3
print("\n 3. \n")
a = eval(input('Enter an interger：'))
b = a + 100
print(a, b)

# 4
# str
print("\n 4. \n")
str1 = 'Hello,'
str2 = 'Python'
str3 = str1 + str2
print(str3)
print()
# var
a = 100
b = 200
c = a + b
print(c)

# 5
print("\n 5. \n")
num1 = eval(input("Enter the 1st intenger:"))
num2 = eval(input("Enter the 2nd intenger:"))
num3 = eval(input("Enter the 3rd intenger:"))
num4 = eval(input("Enter the 4th intenger:"))
num5 = eval(input("Enter the 5th intenger:"))
print(num1, num2, num3, num4, num5)
sum = num1 + num2 + num3 + num4 + num5
print("Sum:{0}".format(sum))
print("Average:{0}".format(sum/5))
