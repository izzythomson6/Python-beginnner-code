#class EmailClient #do not use underscore to separate classes, use capital letter, pascal naming convention
class Point: #we use classes to define new types
    def __init__(self, x, y): #constructor, to create an object
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1= Point(10,20) #classes can also have attibutes we can set anywhere in our programmes
print(point1.x)
point1.draw()

point2 = point()
point2.x = 1
print(point2.x)

#define a new type called person, this person will have attibutes such as name and talk(method)
class Person:
    def __init__(self,name):
        self.name = name #setting the name attribute of the object to the name object passed in this method
    def talk (self):
        print(f"Hi, I am {self.name}")
        print ("talk")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()
#each object is a different incidence of our person class
