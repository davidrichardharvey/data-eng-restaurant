class Table:

    def __init__(self, customers):
        self.customers = customers
        self.bill = []

    def order(self, item, price, quantity = 1):
        self.item = str(item)
        self.price = round(price, 2)
        self.quantity = quantity

        neworder = {"item": self.item, "price": self.price, "quantity": self.quantity}
        i = 0
        appendnew = True
        for x in self.bill:
            comparename = self.bill[i]["item"]
            compareprice = self.bill[i]["price"]

            if self.item == comparename and self.price == compareprice:
                self.bill[i]["quantity"] += self.quantity
                appendnew = False
            else:
                i += 1
        if appendnew == True:
            self.bill.append(neworder)

        return self.bill

    def get_subtotal(self):
        subtotal = 0
        subtotal = sum(self.bill[0:-1]["price"]*self.bill[0:-1]["quantity"]) * self.customers
        return subtotal

New_Table = Table(3)

New_Table.order("Special Fried Rice", 5.8, 2)
New_Table.get_subtotal()

New_Table.order("Special Fried Rice", 5.8, 2)
New_Table.get_subtotal()



