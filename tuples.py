# Tuples in python

# conventionally tuples look like this
Fruit = ("apples", 4, "bananas", 5, "oranges", 6)
# the main difference between tuples and lists is that tuples has () whereas lists have []

lists_of_fruit = ["apples", 4, "bananas", 5, "oranges", 6]

lists_of_fruit[0] = "strawberries"
print(lists_of_fruit)
# we can modify elements within a list
# we cant modify elements within a tuple
# we can perform similar operations on tuples like we can a list
print(Fruit[0:3])
# we can slice a tuple
# concatenation of tuples
Fruit = Fruit[0:4] + ("Cherries", 10)
print (Fruit)
# adds cherries to the code

# tuples with one element in
x = (5, ) #a tuple with one element must be separated by a comma and a space!
print (type(x))

# we can find the length of a tuple
print (len(Fruit))

# creating a tuple
another_tuple = tuple(("Hello", 18, True))
print(type(another_tuple))

# converting a tuple into a list and back into a tuple
Fruit = list(Fruit)
print(type(Fruit))
Fruit.append("Pears")
print(Fruit)
Fruit = tuple(Fruit)
print(Fruit)

#unpacking tuples
Fruit = ("Apples", "Bananas","Pears", "Oranges", "Strawberries")
print(len(Fruit))
(one, two, *three) = Fruit #purely variables, not in quotations therefore not strings
print (one)
print (two)
#an asterick at three assigns three to strawberries, oranges and pears
#one and two will be assigned to apples and bananas
#can move the asterick around, eg if it was on two then bananas, pears and oranges would be assigned to two

#incorporate loops within tuples
for i in range(len(Fruit)):
    print(Fruit[i])
    #will print all the elements within the tuples