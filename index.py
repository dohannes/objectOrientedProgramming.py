class Item:
    pay_rate = 0.8 # creates class attribute; setting pay rate after 20%

    def __init__(self, name: str, pricing: float, quantity=0):
        # assign values to self object
        self.name = name
        self.quantity = quantity
        self.pricing = pricing

        # run validations of recieved arguments using the assert keyword
        try:
            assert quantity >= 0
            assert pricing >= 0
        except AssertionError:
            print(f"pricing and/ or quantity cannot be set to or be less than zero.")
        

    def calculateTotalPrice(self):
        return self.quantity * self.pricing
    
    def applyDiscount(self):
        self.price = self.pricing * self.pay_rate

samsungPhone = Item("smart phone", 800, 5)
iPhonePhone = Item("smart phone", 1200, 10)

# calculate the total price of " " if there is no AssertionError
print(samsungPhone.calculateTotalPrice())

# set the pay rate differently among instance levels
iPhonePhone.pay_rate = 0.3 # set rate to ... %
iPhonePhone.applyDiscount() # apply said discount 
print(iPhonePhone.pricing) # spit out the price of object now