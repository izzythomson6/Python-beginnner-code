#when we use python and want to repeat ourselves
#it is better to use this method so we dont need to keep repeating ourselves
#if something is wrong in the initial code we will not have to change it for every single one

class Mammal:
    def walk(self):
        print("walk")
class Dog(Mammal):
    def bark(self):
        print("bark")
class Cat(Mammal):
    pass #keeps python happy, just means python can skip this line

dog1 = Dog()
