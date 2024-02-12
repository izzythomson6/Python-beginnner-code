#strings

#we have already covered strings, booleans, lists, integers
#integers,flaots and booleans are all considered to be simple date types
#this means they cant be broken down
#lists and strings can be broken down
#they are made up of smaller pieces which can be broken down

#we already know what strings are
print("hello world!")
print(type("hello world"))

#operations on strings
#addition sign concatenation
Greeting = "Helo " #needs a space otherwise joins them both together
Name= "Izzy"
print(Greeting + Name )

print("My shoe size is", 5, "and my age is", 21)

# *operator
print(Greeting*3)
print(Greeting + Name*3)
print((Greeting+Name)*3)

#Index operator
Name = "Brad"
print(Name(2))
print(Name[0]+ Name[3])

#Slicing strings
print(Name[0:2]) #prints br as doesnt include the 2nd element

#lowercase and uppercase
Name= "Izzy"
print(Name).lower
print(Name).upper

#count how many times a character appears in a string
print(Name.count("l"))

#replace specific characters with other characters
print(Name.replace("l", "d"))
Name= ("Izzy")
New_Name= Name.replace("l", "d")
print(New_Name)

#FINDING THE LENGTH OF A STRING
print(len(Name))

#format strings
your_name= input ("your name: ")
Hello= "Hello {}".format(your_name)
print(hello)

#each letter in python is assigned to a specific number
print("orange" < "strawberry")
print(ord("o"))
print(chr(38))

#we can perform maths on strings

#in and not operators
fruit= "banana" #booleans for if a or s are in banana
print("a" in fruit)
print("s" not in fruit)

#incorporate a few things weve learned so far
x= "hello"
y= ""
for character in x:
    y = character.upper() + y
    #if you did y = y + character.upper would get HELLO