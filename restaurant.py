class Table:
    def __init__(self, number_of_customers):
        self.bill = []
        self.customer_number = number_of_customers

    def order(self, item, price, quantity=1):

        # "Expected calling `order` with no quantity to create item with quantity 1."
        # Takes item, price, quantity

        make_order = False

        for i in self.bill:
            if (i['item'] == item) and (i['price'] == price):
                i['quantity'] += quantity
                return make_order
        else:
            return self.bill.append({
                'item': item,
                'price': price,
                'quantity': quantity
            })

    def remove(self, item, price, quantity):

        # "Expected `remove` method to reduce quantity of existing item."
        # Takes item, price, quantity

        remove_order = True
        keep_order = False
        for i in self.bill:
            if (i['item'] == item) and (i['price'] == price):
                if i['quantity'] > quantity:
                    i['quantity'] -= quantity
                    return remove_order
                else:
                    return keep_order
        return keep_order

    def get_subtotal(self):
        # "Expected balance to 2 decimal places to be 50.50."
        total = 0
        for i in self.bill:
            total += (i['price']) * (i['quantity'])
        return round(total, 2)

    def get_total(self, service_charge=0.1):
        # "Expected different dictionary from `get_total`."
        sub = self.get_subtotal()
        return {
            'Sub Total': f'£{sub:.2f}',
            'Service Charge': f'£{sub * service_charge:.2f}',
            'Total': f'£{sub * (1 + service_charge):.2f}'
        }

    def split_bill(self):
        return round(self.get_subtotal() / self.customer_number, 2)


