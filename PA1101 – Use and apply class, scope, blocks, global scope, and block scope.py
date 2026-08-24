'''Exercise 1
Create a global variable and print it inside a function.
'''

name = "Sihle"

def greet():
    print(f"Hello my name is {name}")

greet()

'''
Exercise 2
Create a variable inside an if block and try to access it outside.
Explain the result.
'''

marks = 79
if marks > 75:
        string = "Sihle you have passed the module"
else:
        string = "Sihle you have failed the module"

print(string)

'''
Exercise 3
Create a loop and test whether the loop variable exists outside.
'''

for i in range(3):
    print(f"Inside loop: {i}")

print(f"Outside loop, i is still available: {i}")

# Explanation:
# In Python, the loop variable from a for loop remains accessible
# after the loop finishes. This is different from JavaScript's let,
# where the variable is block-scoped and would not exist outside the loop.

'''
Exercise 4
Create a simple class called Car with a property brand.

Print the brand using a method.'''

class car:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        return f"The brand of the car is: {self.brand}"

my_car = car("BMW")
my_car.show_brand()
