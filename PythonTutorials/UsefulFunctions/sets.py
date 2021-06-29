# a set is a collection which is unordered and un-indexed. They do not allow duplicate values

tools = {"hammer", "axe", "screwdriver", "screwdriver", "screwdriver"} #sets do not allow duplicate values so if i print "screwdriver" more then once, it wont count.
moretools = {"mallet", "saw", "chisel"}

for i in tools:
    print(i) #prints the tools set.
    #it will print it in a random order, since it is unordered and un-indexed

tools.add("jackhammer") #adds an element, jackhammer, to the list.
tools.remove("screwdriver") #removes screwdriver from the list.
tools.update(moretools) #adds everything from the moretools set to the tools set.
all_tools = tools.union(moretools) #creates a new set that has everything from the tools set and moretools set.
print(tools.difference(moretools)) #compares the two, prints what tools have that moretools doesn't 
print(tools.intersection(moretools)) #prints what element they BOTH have, or what they have in common?