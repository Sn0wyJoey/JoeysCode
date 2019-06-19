#!/usr/bin/env python3
import colors as c
name = input(c.green + "What is your name")
age = input(c.magenta + "What is your age")
print(age)
num_age = int(age) #this is the what the age is
#print(c.red + name + c.x + " is going to be", num_age+1,"years old in a year.") 
print("{} {} {} {}" .format(name, "is going to be", num_age+5, "years old in 5 years"))