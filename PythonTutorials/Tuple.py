 #a tuple groups information and is unchangeable (you cant change it)

student = ("Joey", 13, "Male")

print(student.count("Joey")) #prints how many times "Joey" appears in the tuple
print(student.index(13)) #prints the index of 13, which is in the first index so it would print 1.

for i in student:
    print(i) #prints each element in the tuple

if "Joey" in student: #checks if "Joey" is in the tuple
    print("Joey is in the tuple")