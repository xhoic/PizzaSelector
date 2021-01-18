class Pizza:
    '''This class holds data about a product in a store called Alfa.'''

    def __init__(self, name, toppings, qty, size, price):
        self.__name = name
        self.__toppings = toppings
        self.__qty = qty
        self.__size = size
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, toppings):
        self.__toppings = toppings

    @property
    def qty(self):
        return self.__qty

    @qty.setter
    def qty(self, qty):
        self.__qty = qty

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    # get total price
    def total(self, i):
        return self.__price[self.__size[i]] * self.__qty
