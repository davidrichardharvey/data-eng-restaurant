class Table:
    def __init__(self, num_diners):
        self.num_diners = num_diners
        self.bill = []

    def order(self, item, price, quantity=1):
        for entry in self.bill:
            if entry["item"] == item and entry["price"] == price:
                entry["quantity"] += quantity
                return
        self.bill.append({"item": item, "price":price, "quantity": quantity})

    def remove(self, item, price, quantity=1):
        for entry in self.bill:
            if entry["item"] == item and entry["price"] == price and entry["quantity"] <= quantity:
                self.bill.remove(entry)
                return True
            elif entry["item"] == item and entry["price"] == price:
                entry["quantity"] -= quantity
                return True
        return False

    def get_subtotal(self):
        total = 0
        for entry in self.bill:
            total += entry["price"] * entry["quantity"]
        return total

    def get_total(self, charge=0.10):
        st = self.get_subtotal()
        return {"Sub Total": f"£{st:.2f}", "Service Charge": f"£{st*charge:.2f}", "Total": f"£{st*(charge+1):.2f}"}

    def split_bill(self):
        bill = self.get_subtotal() / self.num_diners
        return bill
