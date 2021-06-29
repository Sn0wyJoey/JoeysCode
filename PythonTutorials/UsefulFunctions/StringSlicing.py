#String slicing is creating a substring from another string

#first lets learn about Index[]
# Index[] = Index[start:stop:step]

#In the first perameter, we put the starting index (the index where we start to slice, or start slicing)
#In the second perameter, we put the stopping index (the index where we want end the slice, or stop slicing. That part will not be included.)
#The first index you put in the first perameter is INCLUSIVE. The second index you put in the second perameter is EXCLUSIVE.

name = "Joey Brar" 

last_name = name[5:9] #creates a substring that starts at index 5 and ends at index 9. Since the string ends at 8 and we want to use all of the last name, we put 9, because if we put 8 that would be exlusive and would only be "Bra"
first_name = name[0:4]
print(first_name, last_name)

last_name = name[5:] #if we left the second perameter blank, python will assume the string will continue until the end. This is the same thing as before.
first_name = name[:4] ## if we left the first perameter blank, python will assume it starts at the beggining, 0. This is the same thing as before.
print(first_name)
print(last_name)

#3rd perameter:
count = "123456789"

#if we wanted to count by 2 or 3 instead of 1, then we would use the 3rd index, step.
#step is 1 by default, if we set it to 2, it would count every second character including the first.

count_by_2 = count[0:28:2] #from the first index to the last, it goes by 2 and skips one, starting from one.
print(count_by_2)

count_by_2 = count[::2] #if we put the first and second perameters blank, it would count from the start to the end of the string.
print(count_by_2)

reversed_count = count[::-1] #counts by -1 and reverses the string.
print(reversed_count)

#Now lets learn about slice()
print("\n")

website = "http://google.com"
#for this, we want to create a second string that shows only the google, not the http:// and .com

#first, create a slice object. Lets name it as slice. We need to put a start, a stop, and a step. Sort of like the index function but seperated with commas.

#the website name starts at index 7, after the http://, but there are many different websites with different names, and we don't know how long the name is, so we don't know how long to slice.
#solution: we can just remove the .com part. How? Each character has both a positive index and a negative index.
#The positive index starts from the left, and the negative index starts from the right (at the end of the string). The negative index starts at -1, and the positive index starts at 0.

#String "Joey Brar": "J  o  e  y     B  r  a  r"
#Positive Index:      0, 1, 2, 3, 4, 5, 6, 7, 8
#Negative Index:      -9,-8,-7,-6,-5,-4,-3,-2,-1

#its as if we are counting backwards. For slicing, we can use a combination
#of positive index and negative index to slice out the .com part at the end.

slice = slice(7, -4)

website1 = "http://wikipedia.com"
website2 = "http://youtube.com"

#applying the slice object:

print(website[slice])
print(website1[slice])
print(website2[slice])