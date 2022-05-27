class Table:
    def __init__(self, num_guests):
        self._bill = []
        self._num_guests = num_guests

    def order(self, item, price, quantity=1):
        for order_item in self._bill:
            if order_item['item'] == item and order_item['price'] == price:
                order_item['quantity'] += quantity
                return None
        self._bill.append({
            'item': item,
            'price': price,
            'quantity': quantity
        })

    def remove(self, item, price, quantity):
        for order_item in self._bill:
            if order_item['item'] == item and order_item['price'] == price:
                if order_item['quantity'] > quantity:  # reduce quantity be specified amount
                    order_item['quantity'] -= quantity
                    return True

                elif order_item['quantity'] == quantity:  # quantity would be zero so remove item from bill
                    self._bill.remove(order_item)
                    return True

                else:  # specified quantity was more than already on the bill
                    return False
        return False  # method hasn't yet returned so the specified item doesn't exist

    def get_subtotal(self):
        total = 0
        for order_item in self._bill:
            total += order_item['price'] * order_item['quantity']
        return total

    def get_total(self, service_charge=0.1):
        sub = self.get_subtotal()
        return {
            'Sub Total': f'£{sub:.2f}',
            'Service Charge': f'£{sub * service_charge:.2f}',
            'Total': f'£{sub * (1 + service_charge):.2f}'
        }

    def split_bill(self):
        return round(self.get_subtotal() / self._num_guests, 2)
