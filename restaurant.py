class Table:

    def __init__(self, guest):
        self.bill = []
        self.guest = guest

    def order(self, item, price, quantity=1):

        for food in self.bill:
            if food['item'] == food and food['price'] == price:
                food['quantity'] += quantity
            else:
                self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity):
        no_food = False
        good_food = True
        for food in self.bill:
            if food['item'] == item and food['price'] == price:
                if food['quantity'] > quantity:
                    food['quantity'] -= quantity
                    return good_food
                else:
                    return no_food
        return no_food

    def get_subtotal(self):
        subtotal = 0
        for food in self.bill:
            subtotal += food['price'] * food['quantity']
            subtotal.__round__(2)
        return subtotal
        # method that returns the total cost for the table
        # based on the prices and quantities in the bill

    def get_total(self, service=0.1):
        total = self.get_subtotal()
        return {
            'Sub Total': f'£{total:.2f}',
            'Service Charge': f'{total * service:.2f}',
            'Total': f'£{total * (1 + service): .2f}'
            }

    def split_bill(self):
        return round(self.get_subtotal()/self.guest, 2)



