#nested function calls are function calls inside of other function calls. The innermost function calls are
#resolved first. The returned value is used as an argument for the next outer function.

#Example:

num = input("Enter a positive number: ")
num = float(num)
num = abs(num)
num = round(num)

print(num) 

print("\n")
# we can make this shorter:

print(round(abs(float(num)))) #should print the same thing as before, but shorter