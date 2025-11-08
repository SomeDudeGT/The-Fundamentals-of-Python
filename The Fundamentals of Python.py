# The Fundamentals of Python


#1. Variables
x = "Hi guys its me SomeDude!"
print(x)



#2. Loops
for i in range(10):  # starts at 0 all the way up to 9
    print(i)



#3. Functions
def add(a, b):
    return a + b

print(add(1, 2))



#4. classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

p = Person("SomeDude", 30)
print(p)





#5. Exceptions
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")




#6. file handling
with open("test.txt", "w") as f:
    f.write("hello world")

with open("test.txt", "r") as f:
    print(f.read())




#7. Modules
import math
print(math.sqrt(16))