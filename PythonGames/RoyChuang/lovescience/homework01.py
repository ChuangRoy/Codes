# 1
print(" 1.\n")
str1 = """ 
-----------------
"Python" is fun !
-----------------
"""
print(str1)

# 2
print("\n 2.\n")
print("{0:7d} {1:7d} {2:7d}".format(12345,12,123))
print("{0:7d} {1:7d} {2:7d}".format(12,123,12345))

# 3
print("\n 3. \n")
print(format(12345,">7d"))
print(format(12,">7d"))
print(format(1234567,">7d"))

# 4
print("\n 4. \n")
print("%8.2f"%(123.45))
print("%8.2f"%(12345.67))
print("%8.2f"%(12.35))

#5
print("\n 5. \n")
print("{0:12s} , {1}".format("Member Karen","discount 0.35"))
print("{0:12s} , {1}".format("Member Sammy","discount 0.40"))
print("{0:12s} , {1}".format("Member JoJo","discount 0.42"))