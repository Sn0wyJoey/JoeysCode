#A dictionary is a changeable, unordered collection of unique key value pairs. They are fast because they use hashing and allows us to access a value quickly.

capitals = {"USA" : "Washington DC",
            "India" : "New Dehli",
            "China" : "Beijing",
            "Russia" : "Moscow"} #the first part in x : y, x is the key, y is the value.

print(capitals["Russia"]) #prints the value stored or associated with Russia, which is Moscow.
#If we did this for a country that is not in the dictionary, like germany, we would ge an error. So, we can do:
print(capitals.get("Germany")) #If there is no germany in the dictionary, it would print None.
print(capitals.keys()) #prints only the keys and not the values
print(capitals.values()) #prints only the values and not the keys
print(capitals.items()) #prints both the keys and the values
capitals.update({"Germany" : "Berlin"}) #Adds Germany to the dictionary as a key and gives it the value Berlin
capitals.update({"USA" : "Las Vegas"}) #Updates the key of USA to have the value of Las Vegas
capitals.pop("India") #Removes India from the dictionary
capitals["Taiwan"] = capitals.pop("China") #Adds a new key called Taiwan and makes it have the same value as China, then deletes China. Its basically like switching from China to Taiwan.

for key, value in capitals.items(): #iterates once for each key value pair in the dictionary
    print(key, ":", value) #prints the entire dictionary on separate lines

capitals.clear() #removes everything from the dictionary.

print(capitals)
