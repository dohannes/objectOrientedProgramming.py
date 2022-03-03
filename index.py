"""
4 Principales of Object Oriented Programming:

--Encapsulation:
    Refers to the restriction of the direct access to some of our attributes. 
    -- we can add restrictions to our code that it needs to run through before we can alter some attribute. 
       Ex: self.__name = name; we cannot alter this code following an assignement.

    -- We disallow direct access to attributes in the instance, unless we directly access a property decorator.
        -> We can modify values of these attributes, by accessing direct methods that allow us to; ex: applyIncrement.

--Abstraction:
    Shows only the necessary attributes of a created instance, hiding the unnecessary ones.
    --Purpose: Hiding uneccessary details from us users.

-- Inheritance:
    Ability to reuse code we've already created, just like we created child classes that derive off of the parent class Item.

-- Polymorphism:
    Refers to the use of a single type entity, to represent different types in different scenarios.
"""
import csv

class Item:
    pay_rate = 0.8 # creates class attribute; setting pay rate after 20%
    all = [] # allows us to append all elements to this

    def __init__(self, name: str, pricing: float, quantity=0, broken=0):
        # assign values to self object
        self.__name = name # to create a read only attribute, we must add a SINGLE UNDERSCORE to the beginning.
        self.quantity = quantity
        self.__pricing = pricing
        self.broken = broken

        # run validations of recieved arguments using the assert keyword
        try:
            assert quantity >= 0
            assert pricing >= 0
            assert broken >= 0
        except AssertionError:
            print("pricing and/ or quantity cannot be set to or be less than zero.")

        # actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__pricing
    
    def applyDiscount(self):
        self.__pricing = self.__pricing * self.pay_rate
    
    def applyIncrement(self, increment_value):
        self.__pricing = self.__pricing + self.__pricing * increment_value
    @property
    # Property decorator = Read-Only attribute
    # this decorator is seen as a getter. 
    def name(self):
        # print("You're trying to get the name") # this line will execute, before the setter decorator
        return self.__name
    
    @name.setter
    # this decorator is seen as a setter.
    # allows us to set the "read-only" attribute to a new 'value'
    # you can use setters to restrict data you/your user are attempting to grab
    def name(self, value):
        if isinstance(value, str):
            # lets restrict the length of characters for new name:
            if len(value) < 8:
                # raise Exception("Name length cannot be less than 8 characters."); This will raise a custom exception in our code; The code below is nicer though.
                print("Name length cannot be less than 8 characters.")
            else:
                self.__name = value # otherwise, set the new "private" attribute to the inputted value.
        else:
            print("Name cannot be an integer. Please change this parameter.")
        
    def calculateTotalPrice(self):
        return self.quantity * self.__pricing

    # 'representative' magic function:
    def __repr__(self):
        return f"Item('{self.name}', {self.__pricing}, {self.quantity})"

    # decorator to make the code below a class method
    
    """
    class methods call the instance of the class, as a parameter to the function
      i.e. Item.instantiateFromCSV("Item"), the function will take in Item as a parameter, as it is a classmethod
    """
    
    @classmethod
    def instantiateFromCSV(cls):
        with open("items.csv", "r") as detailedCSV:
            reader = csv.DictReader(detailedCSV)
            items = list(reader) # converts reader into a list
        
        for item in items:
            print(item)
            #   why doesn't this work?
            # Item(
            #     name=item.get('name'),
            #     pricing=float(item.get('pricing')),
            #     quantity=float(item.get('quantity'))
            # )

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are .0
        #   ex: 5.0 10.0 25.0
        if isinstance(num, float): # checks if the recieved parameter is an instance of a float or an integer
            # counts out the floats that are point 0
            return num.is_integer() # should check if the float is a .0
        elif isinstance(num, int):
            return True
        else:
            return False
    
    def calculateQualityControl(self):
        quantity = self.quantity
        broken = self.broken

        percentage = (broken/quantity)*100

        print(f"{round(percentage, 2)}% of '{self.name}' are broken") # rounds the decmial to 2 rather than 'n' points.

# ----------------------------------------------------------------------------------------------------------------------
#           Example of Abstraction: Doesn't need to be accessed by the user, can be sent through the body of code in our object.
#               -> The addition of '__', makes the functions invisible to the user
    def __constructBody(self):
        return f"""
        Hello, ...
        We have {self.name.upper()}, in stock! ({self.quantity} items).
        Regards,
        Micheal.
        """

    def __connect(self):
        pass

    def __send(self):
        pass

    def sendEmail(self):
        self.__constructBody()
        self.__connect()
        self.__send()

class Phone(Item):
    # we recieve the exact same parameters from the previous Parent Class
    
    all = [] # allows us to append all elements to this array

    # we dont need to copy and paste the parameters from the Parent Class, instead we can use the kwargs parameter
    def __init__(self, name: str, pricing: float, quantity=0, broken=0):
        super().__init__(name, pricing, quantity, broken)
        Phone.all.append(all)

class Laptop(Item):
    all = []
    def __init__(self, name: str, pricing: float, quantity=0, broken=0):
        super().__init__(name, pricing, quantity, broken)
        Laptop.all.append(all)
    
# -------------------------------------------------------------------------------------------

# here is the code to run to get all the names of instance:
# print(Item.allElements) # allows us to print all the created instances from the Class Level
# for instance in Item.allElements:
#     print(instance.name)

# calculate the total price of " " if there is no AssertionError
# print(samsungPhone.calculateTotalPrice())

# # set the pay rate differently among instance levels
# iPhonePhone.pay_rate = 0.3 # set rate to ... %
# iPhonePhone.applyDiscount() # apply said discount 
# print(iPhonePhone.pricing) # spit out the price of object now

# print(Item.is_integer(7.5)), will check if integer or not
# print(Item.instantiateFromCSV())