class Customer:
    all_customers=[]

    def __init__(self,name):
        self.name=name
        self.name=None
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name
        
    @name.setter 
    def name(self,name):
        if not  isinstance(name,str) :
            raise ValueError("Name must be a string ")
        if not (1<= len(name.strip())<= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name=name
        pass



    # Return all orders belonging to this customer
    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.customer is self]

    # Return unique list of coffees this customer has ordered
    def coffees(self):
        return list({order.coffee for order in self.orders()})

    # Let a customer create an order
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    # Return the customer who has spent the most on a given coffee
    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order

        spending = {}

        for order in Order.all_orders:
            if order.coffee is coffee:
                spending[order.customer] = spending.get(order.customer, 0) + order.price

        if not spending:
            return None

        # Return customer with highest total
        return max(spending, key=spending.get)
    pass

