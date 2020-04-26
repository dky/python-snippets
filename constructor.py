"""
Constructor - Used for instantiating an object, the task of constructors is to
initialize(assign values) to the data members of the class when an object of
the class is created.
"""


class Geek:
    # default Constructor
    def __init__(self):
        self.geek = "Geek"

    # method for printing data members
    def print_Geek(self):
        print(self.geek)


# creating object of the class
ob = Geek()
ob.print_Geek()
