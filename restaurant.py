class Table:
    def __init__(self, people):
        self.people = people
        self.bill = []

    def order(self, item, price, quantity=1):
        if len(self.bill) != 0:
            for i in self.bill:
                if i['item'] == item:
                    i[quantity] += quantity
                    break
        self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity):
        for i in range(len(self.bill)):
            current_dict = self.bill[i]
            if current_dict['item'] == item and current_dict['price'] == price:
                if current_dict['quantity'] < quantity:
                    return False
                elif current_dict['quantity'] - quantity == 0:
                    self.bill.pop(i)
                    return True
                else:
                    current_dict['quantity'] -= quantity
                    return True
            else:
                return False

    def get_subtotal(self):
        total = 0
        for i in self.bill:
            total += i['quantity'] * i['price']

        return total

    def get_total(self, service_charge_rate=0.10):
        if isinstance(service_charge_rate, float):
            sub_total = self.get_subtotal()
            service_charge = self.get_subtotal() * service_charge_rate
            total = sub_total + service_charge

            return {"Sub Total": f'£{sub_total:.2f}', "Service Charge": f'£{service_charge:.2f}',
                    "Total": f'£{total:.2f}'}

    def split_bill(self):
        return round(self.get_subtotal()/self.people, 2)
