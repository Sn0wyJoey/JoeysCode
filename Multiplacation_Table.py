import colors as c
Num = input("What number should we use?")
Lines = input("How many lines should we use for the multiplucation table?")
for count in range(1, int(Lines) + 1):
    print(" {} * {} = {}".format (count , Num , int(Num) * count))