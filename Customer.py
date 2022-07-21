class Customer:
    def __init__(self,last_name, first_name= None):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def equals(self,customer):
        return self.last_name == customer.get_last_name() and self.first_name == customer.get_first_name()

    def __str__(self):
        return str(self.last_name) +"," + str(self.first_name)
