class Table:
      def __init__(self, diners):
        self.bill = []
        self.diners = diners

    def order(self, item, price, quantity=1):
        for order_item in self.bill:
            if order_item["item"] == item and order_item["price"] == price:
                order_item["quantity"] += quantity
                return None

        add_bill = {"item": item, "price": price, "quantity": quantity}
        self.bill.append(add_bill)

    def remove(self, item, price, quantity):
        for order_item in self.bill:
            if order_item["item"] == item and order_item["price"] == price:
                if order_item["quantity"] < quantity:
                    return False
                elif order_item["quantity"] == 0:
                    self.bill.remove(order_item)
                else:
                    order_item["quantity"] -= quantity
                return True
            else:
                return False

    def get_subtotal(self):
        total = 0
        for order_item in self.bill:
            total += order_item['price'] * order_item['quantity']
        return total
