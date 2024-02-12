#python types- booleans, strings, integers, floats

print(type("Hello world"))
print(type(13))
print(type(4.72))
print(type(True))

#Moving to integers
print(4.72, int(4.72)) #python rounds down
print(4.05,int(4.05))

#rounding up
print(4.72, int(4.72), int(round(4.72)))

#moving strings to integers
print("12345", int("12345"))
print(type("12345")) #tells you its a string
print(type(int("12345"))) #tells you its an integer

#moving to floats
print(float(18))
print(float(12345)) #comes up with the decimal

#moving to strings
print(str(18))
print(str(19.5))
print(type(str(19.5)))

#logical operators
#there are three different logical operators- and , or and not

x=6
print(x > 0 and x < 10)
#print (0 < x < 10)

y = 23
print (y % 2 == 0 or y % == 5) #will say true because its one or the other
#and is saying both of the things must be true