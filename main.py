# python conditions
# n = int(input("Number: "))

# if n > 0:
#     print("n is positive")
# elif n < 0:
#     print("n is negative")
# else: 
#     print("n is zero")

# Sequences
# Define a list of names
# names = ["Chad", "Ron", "Tom", "Comet"]

# names.append("Drake")

# names.sort()

# print(names)

#Create an empty set
# s = set()

#add elements to set
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(4)


# s.remove(2)

# print(f"The set has {len(s)}")

# loops
# for i in [0, 1, 2, 3, 4, 5]:    
#     print(i)

#Dictionaries
# houses = {"Harry": "Griffyndor", "Draco": "Slytherin"}

# houses["Homie"] = "Gryffindor"

# print(houses["Homie"])

#Functions 
# def square(x):
#     return x * x

# for i in range(10):
#     print(f"The square of {i} is {square(i)}")

#Classes

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p = Point(2, 8)
# print(p.x)
# print(p.y)

#OOP in Python

# class Flight():
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []

#     def add_passenger(self, name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True

#     def open_seats(self):
#         return self.capacity - len(self.passengers)


# flight = Flight(3)

# people = ["Han", "Ron", "Marshall", "Chad"]
# for person in people:
#     success = flight.add_passenger(person)
#     if success: 
#         print(f"added {person} to flight successfully")
#     else:
#         print(f"No available seats for {person}")

#Decorators
        
# def announce(f):
#     def wrapper():
#         print("about to run function")
#         f()
#         print("Done with the function")
#     return wrapper

# @announce
# def hello():
#     print("Hello World")

# hello()

#lambda

# people = [
#     {"name": "Harry", "house": "Griffyndor"},
#     {"name": "Cho", "house": "Ravenclaw"},
#     {"name": "Draco", "house": "Slytherin"}
# ]


# people.sort(key = lambda person: person["name"])

# print(people)

#Exceptions
x = int(input("x: "))
y = int(input("y: "))

result = x / y

print(f"{x} / {y} = {result}")
