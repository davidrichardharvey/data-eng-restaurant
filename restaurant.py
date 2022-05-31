class Table:

    def __init__(self):
        self.bill = []

    def order(self, item, price, quantity=1):

        for item in self.bill:
            if item['item'] == item and item['price'] == price:
                item['quantity'] += quantity
            else:
                self.bill.append({"item": item, "price": price, "quantity": quantity})

        # variables items, price and quantity
        # quantity should be defaulted at 1
        # the items on the bill should be appended to a dictionary
        # update the quantity to the bill if needed
        pass

    def remove(self):
        # same sort of principle as order but should remove the quantity
        # if the quantity is 0 remove it off the bill completely
        #  return True unless there is not an item with the corresponding item name and price
        # return False and make no change to the bill.
        pass

    def get_subtotal(self):
        # method that returns the total cost for the table
        # based on the prices and quantities in the bill
        pass

    def get_total(self):
        # return a dictionary with the
        # following keys: Sub Total, Service Charge, Total

        # The values should be string representations of
        # the corresponding prices in British pounds and pence

        pass

    def split_bill(self):
        # which returns the the subtotal cost of the bill
        # divided by the number of diners as a float rounded up to the nearest penny.
        pass

    pass
