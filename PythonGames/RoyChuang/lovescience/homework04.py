# 1
print("1. \n")
num1, num2 = 100, 3
print("num1 % num2 = ", num1 % num2)
print("num1 * num2 = ", num1*num2)
print("num1 / num2 = ", round(num1/num2, 3))
print("num1 // num2 = ", num1//num2)
print("\n")

# 2
print("2. \n")
a = eval(input("Input An Intenger:"))
b = eval(input("Input An Intenger:"))
c = eval(input("Input An Intenger:"))
d = eval(input("Input An Intenger:"))
e = eval(input("Input An Intenger:"))
print("The five numbers are:", a, b, c, d, e)
print("The sum of them are:", a+b+c+d+e)
print("The average of them are {0:<7.3f}".format((a+b+c+d+e)/5))
print("\n")

# 3
print("3. \n")
width = eval(input("Width:"))
height = eval(input("Height:"))
print("The width is ",width)
print("The height is ",height)
print("The perimeter is ",(width+height)*2)
print("The area is ",width*height)