#lists store multiple items in a single variable

food = ["pizza", "hamburgur", "sushi", "cheese"]

print(food) #prints the whole list
print(food[0]) #prints the first item in the list
print(food[1]) #prints the second item in the list
# print(food[4]) #gives an error because there aren't 4 items. it would be out of range

food[0] = "bread" #changes the first item on the list to bread.
print(food[0]) #prints bread

print("\n") # new line

for i in food:
    print(i) #prints everything in the food list.

#useful functions:
food.append("ice cream") #adds ice cream to the list
food.remove("hot dog") #removes hotdog from the list
food.pop() #removes the last element of the list.
food.insert(0, "cake") #adds cake to the 0th index in the list
food.sort() #sorts the list alphabetically
food.clear() #removes all of the elements in the list