class Coffee:
    all_coffees = []

    def __init__(self, name):
        self._name = None
        self.name = name
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string")
        name = name.strip()
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = name

    # Return all orders for this coffee
    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.coffee is self]

    # Return unique list of customers who ordered this coffee
    def customers(self):
        return list({order.customer for order in self.orders()})

    # Number of orders for this coffee
    def num_orders(self):
        return len(self.orders())

    # Average price of this coffee
    def average_price(self):
        orders = self.orders()
        if not orders:
            return None
        return sum(order.price for order in orders) / len(orders)
