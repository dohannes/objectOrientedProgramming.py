from index import Item
class Keyboard(Item):
    pay_rate = 0.5 # overwriting in the child class is legal
    # we dont need to copy and paste the parameters from the Parent Class, instead we can use the kwargs parameter
    def __init__(self, name: str, pricing: float, quantity=0):
        super().__init__(name, pricing, quantity)