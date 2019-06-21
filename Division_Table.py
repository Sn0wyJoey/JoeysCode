import colors as c
Space = (" >")
Num1 = input("What number should we use?" + Space)
Line1 = input("How many lines should we use for the division table?" + Space)
for count in range(1, int(Num1) + 1):
    print(" {} / {} = {}".format (count , Num1 , int(Num1) / count))

    