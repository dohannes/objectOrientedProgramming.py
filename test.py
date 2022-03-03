from index import Item
from index import Laptop # used to show inheritance from previous classes


samsungPhone = Item("SamsungS20", 750, 10, 3)

# --------------------------------
#   -> Examples of Encapsulation

# samsungPhone.applyIncrement(0.2)
# samsungPhone.applyDiscount()
# print(samsungPhone.price)

# --------------------------------
#   -> Examples of Abstraction:

# samsungPhone.__connect(); This is now seen as a private method; 

# -------------------------------
#   -> Example of Abstraction

# lenovoLaptop = Laptop("Lenovo T470", 850, 20, 7)
# lenovoLaptop.applyIncrement(0.2)
# print(lenovoLaptop.price)

