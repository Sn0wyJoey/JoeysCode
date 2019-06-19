#!/usr/bin/env python
import colors
yes = input("Do you like sports?")
if yes == "yes" or yes == "Yes" or yes == "yea" or yes == "Yea":
    grade = input("Are you in middle school?")
    if grade == "yes" or grade == "Yes" or grade == "yea" or grade == "Yea":
        print("You are Joey")
        print("You lost")
        exit()
    else:
        print("You are Peter")
else: 
    input("are you Raayan?")
    if yes == "yes" or yes == "Yes" or yes == "Yea" or yes == "yea":
        print("You lost!")
        exit()
    else:
        print("You won!")
        exit()
