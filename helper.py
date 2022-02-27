# when to use a class or static method

"""
BIG MAIN DIFFERENCE:
    -- Static method doesn't take in the object instance as a parameter, but a class method does.
        A static method can take in new parameters that don't require the 'self' keyword.
"""

class Item:
    @staticmethod
    # regular parameters are given into this method
    def is_integer(num):
        pass
        """
        This should do something that has a relationship with the class, but not something that must be unique per instance
        """

    @classmethod
    def instantiate_from_something(cls):
        """
        Use this to do something that has a relationship with the class, but usually, those are used to maniuplate different sttructures
        of data instantiate objects, like we have done with the previous CSV file.
        Maintain data in 
        """

# these methods can be called from instances, other than just the class level
# won't throw any errors
item1 = Item()
item1.is_integer(5)
item1.instantiate_from_something()