from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self,customer,coffee,price):
        self.customer=customer
        self.coffee=coffee
        self.price=price

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self,customer):
        if not isinstance (customer in Customer):
            raise ValueError("customer must be an instance of Customer.")
        self._customer=customer


    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self,coffee):
        if not isinstance(coffee,Coffee):
            raise ValueError("coffee must be an instance of Coffee")
        self._coffee=coffee

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price (self,price):
        if not isinstance(price,(float,int)):
            raise ValueError("price must be a number")
        if price < 1.0 or price >10.0:
            raise ValueError("price must be between 1.0 and 10.0.")





    pass