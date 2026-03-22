#HI-CAS (Automated Household Inventory & Consumption Analytics System)
from datetime import datetime, timedelta
class Item:
    def __init__(self, name, qty, exp_days):
        self.name = name
        self.qty = qty
        self.expiry = datetime.now() + timedelta(days=exp_days)
        self.used = 0
class HICAS:
    def __init__(self):
        self.inv = {}
    def add(self, name, qty, exp):
        if name in self.inv:
            self.inv[name].qty += qty
        else:
            self.inv[name] = Item(name, qty, exp)
        print("Item added!")
    def use(self, name, amt):
        if name in self.inv and self.inv[name].qty >= amt:
            self.inv[name].qty -= amt
            self.inv[name].used += amt
            print("Item used!")
        else:
            print("Not enough stock / Item missing!")
    def show(self):
        print("\nInventory:")
        for i in self.inv.values():
            print(i.name, "| Qty:", i.qty, "| Exp:", i.expiry.date())
    def alerts(self):
        print("\nAlerts:")
        for i in self.inv.values():
            if i.qty <= 2:
                print("Low stock:", i.name)
            if (i.expiry - datetime.now()).days <= 2:
                print("Expiring soon:", i.name)
            else:
                print("No alerts / expiry nearby")
    def analytics(self):
        print("\nUsage:")
        for i in self.inv.values():
            print(i.name, "used:", i.used)
    def consumption_analysis(self):
        print("\nConsumption Analysis:")
        for i in self.inv.values():
            if i.used > 10:
                level = "High consumption"
            elif i.used > 5:
                level = "Moderate consumption"
            elif i.used > 0:
                level = "Low consumption"
            else:
                level = "No usage yet"

            print(i.name, "| Used:", i.used, "| Remaining Qty:", i.qty, "->", level)
h = HICAS()
while True:
    print("\n1.Add \n2.Use \n3.Show \n4.Alerts \n5.Consumption \n6.Consumption Analysis \n7.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        h.add(input("Name: "), int(input("Qty: ")), int(input("Expiry days: ")))
    elif ch == 2:
        h.use(input("Name: "), int(input("Amount: ")))
    elif ch == 3:
        h.show()
    elif ch == 4:
        h.alerts()
    elif ch == 5:
        h.analytics()
    elif ch == 6:
        h.consumption_analysis()
    elif ch == 7:
        break
    else:
        print("Invalid!")
