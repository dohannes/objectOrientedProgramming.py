"""
--Polymorphism (Poly- many; Morphism- forms)
Refers to the use of a single type entity, to represent different types in different scenarios.

    -- Often, Polymorphism and Inheritance are linked together cause they affect the same things
"""
from index import Item
from keyboard import Keyboard
# name = "Dean"
# print(len(name)) # perfect representation of what polymorphism is; outputs 4, referring to the characters in the string

# ourList = ["Michael", "Jackson"] 
# print(len(ourList)) # again, another representation of what polymorphism is; outputs 2 referring to the amount of elements in the array.

# samsungPhone = Phone("SamsungS20", 600, 20, 5) # creation of our instance
# samsungPhone.applyDiscount() # this method can be accessed from all kinds of objects. Not only Item, Phone or Laptop
# print(samsungPhone.price)

# you can have the control to change the value of discount, just like we did in the child class in keyboard.py;
# this action is legal in python, and is a form of polymorphism
logitechKeyboard = Keyboard("Logic Keyboard", 20, 10)
logitechKeyboard.applyDiscount()
print(logitechKeyboard.price)