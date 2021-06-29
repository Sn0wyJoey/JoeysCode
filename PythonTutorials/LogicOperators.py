temp = int(input("What is the temperature outside? (in celcius): "))
num = int(input("Pick a number: "))

if temp >= 0 and temp <= 30: #uses the (and) operator, if a is true AND b is true (only if both conditions are true)
    print("The temperature is good today!\nGo outside!")
elif temp < 0 or temp > 30: #uses the (or) operator, if a is true OR b is true (as long as one condition is true)
    print("The temperature is bad today :(\nDon't go outside.")

if not(num < 0 and num > 100): #This is the (not) operator, if the condition is false, it makes it true. If the condition is true, it makes it false.
    print("Your number is between 1 and 100")
elif not(num >= 0 and num <= 100):
    print("Your number is not in between 1 and 100")

    

