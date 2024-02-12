#mini project- random password generator

#importing the relevant modules
from random import randint

#ALL uppercase password
password = "" #emptystring
for i in range (10):
    i = chr(randint(65,90))
    password = str(password) + i #a for loop that goes round until it reach 10 letter uppercase password
print(password)

#upper and lower case password
password = ""
for i in range(5): #range 5 because it adds a uppercase and lower case each time the loop repeats- equals to ten
    i = chr(randint(65,90)) #accounts for the uppercase characters
    for j in range(5):
        j= chr(randint(65,90)).lower()
    password= str (password) + i + j
    print (password)
    #this produces a password that is upper case and lower case and random letters