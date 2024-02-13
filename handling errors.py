try:
     age = int(input("Age: ")) #needs to be stored as an int function and in a variable called age
     income = 20000
     risk = income / age
     print(age)
except ZeroDivisionError: #cant divide a number by zero if you input age as zero
    print("Age can't be zero")
except ValueError:
       print("Invalid value") #putting a value which isnt numerical for age
