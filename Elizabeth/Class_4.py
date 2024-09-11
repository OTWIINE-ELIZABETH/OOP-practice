

# Class: Person
class Person:
    # Attributes: name, age
    def __init__(self, name, age):
        # Initialize attributes
        self.name = name
        self.age = age

    # Method: introduce_yourself()
    def introduce_yourself(self):
        # Print an introduction message
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")