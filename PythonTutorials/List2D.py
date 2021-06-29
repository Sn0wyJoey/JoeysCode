#2d lists are a list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "rice"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]
print(food) #prints the 2d list

#print(food[x, y]) x, the first perameter is the list we want. y is the element we want in the list we put before.
print(food[0][1]) #prints soda