class Table:
    def __init__(self, people_count):
        self.people_count = people_count
        self.bill = []

    # create dict for the item, if item/price exists: increase quantity, else append to bill list
    def order(self, item_name, price, quantity=1):
        exists, location = self.check_if_item_exist(item_name, price)
        if exists:
            new_quantity = self.bill[location]["quantity"] + quantity
            self.bill[location] = {"item": item_name, "price": price, "quantity": new_quantity}
        else:
            order_add = {"item": item_name, "price": price, "quantity": quantity}
            self.bill.append(order_add)

    # split the bill by people count
    def split_bill(self):
        return round(self.get_subtotal() / self.people_count, 2)

    # create a dict with formatted items that show the totals
    def get_total(self, tip_perc=0.1):
        subtotal = self.get_subtotal()
        total = {"Sub Total": f"£{subtotal:>.2f}",
                 "Service Charge": f"£{subtotal * tip_perc:>.2f}",
                 "Total": f"£{subtotal * (1 + tip_perc):>.2f}"}
        return total

    # simple sum of -> product of each item/quantity pair
    def get_subtotal(self):
        subtotal = 0
        for each_item in self.bill:
            subtotal += each_item["price"] * each_item["quantity"]
        return subtotal

    # adjust the item quantity, or remove it if <= 0
    def remove(self, item_name, price, quantity):
        exists, location = self.check_if_item_exist(item_name, price)
        if exists:
            new_quantity = self.bill[location]["quantity"] - quantity
            # reject the method if the result is negative quantity
            if new_quantity < 0:
                return False
            # special case, remove the item if quantity set to 0
            elif new_quantity == 0:
                del self.bill[location]
            else:
                self.bill[location] = {"item": item_name, "price": price, "quantity": new_quantity}
            return True
        return False

    # return if an item exists, and its location
    def check_if_item_exist(self, item_name, price):
        exists = False
        location = -1
        for index, value in enumerate(self.bill):
            if value["item"] == item_name and value["price"] == price:
                exists = True
                location = index
                break
        return exists, location
