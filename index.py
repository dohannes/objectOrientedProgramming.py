import csv

class Item:
    pay_rate = 0.8 # creates class attribute; setting pay rate after 20%
    all = [] # allows us to append all elements to this

    def __init__(self, name: str, pricing: float, quantity=0, broken=0):
        # assign values to self object
        self.name = name
        self.quantity = quantity
        self.pricing = pricing
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
        
    def calculateTotalPrice(self):
        return self.quantity * self.pricing
    
    def applyDiscount(self):
        self.price = self.pricing * self.pay_rate

    # 'representative' magic function:
    def __repr__(self):
        return f"Item('{self.name}', {self.pricing}, {self.quantity})"

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
    
phone1 = Phone("samsungPhoneS20", 750, 37, 15)
phone2 = Phone("samsungPhoneS21", 1000, 15, 7)

phone1.calculateQualityControl()

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