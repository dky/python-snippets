# Declaring a class. This class is named Vehicle.
# The object is what the class is based upon or inhertiting from - This is
# known as the base class or the parent class.

"""
class Vehicle(object):

    def __init__(self):
        # Init method is only called once and is not to be called again inside
        # the program. This is also known as the constructor
        pass
"""

# In Python 3 we can also declare a class as follows:
# Notice we don't have say we are inherting from an object.


class Vehicle:

    def __init__(self, color, doors, tires):
        # constructor
        self.color = color
        self.doors = doors
        self.tires = tires

    # Methods, they are "methods once they live in a class"
    # Also notice every method has to have at least one argument self.
    # This is not true with a function.
    def brake(self):
        # stop the car
        return "Braking"

    def drive(self):
        # drive the car
        return "I'm driving"
