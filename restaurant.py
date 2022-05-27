class Table:
    def __init__(self, people_count):
        self.people_count = people_count
        self.bill = []

    # create dict for the item, hence append to bill list
    def order(self, item_name, price, quantity=1):
        order_add = {'item': item_name, 'price': price, 'quantity': quantity}
        self.bill.append(order_add)

    # split the bill into.... the number of the table??? (assume it's people count)
    def split_bill(self):
        return self.get_subtotal() / self.people_count

    # create a dict with formatted items that show the totals
    def get_total(self, tip_perc):
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

    # find the item, hence adjust quantity, hence stop searching
    def remove(self, item_name, price, quantity):
        for i in self.bill:
            if i["item"] == item_name and i["price"] == price:
                i["quantity"] -= quantity
                break
