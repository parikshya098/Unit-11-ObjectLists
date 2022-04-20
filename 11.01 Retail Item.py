class RetailItem: 
    def __init__(self, Description='', UnitOnHand=0, Price=0): 
        self.Description = Description 
        self.UnitOnHand = UnitOnHand 
        self.Price = Price 
    def InventoryValue(self): 
        return (self.UnitOnHand * self.Price) 
inventoryfile = open("11.01 Inventory.txt","r")
inventorylist = []
x = inventoryfile.readline()
while x !="":
    description, unit_on_hand, price = x.split(",")
    item = RetailItem(description, int(unit_on_hand), float(price))
    inventorylist.append(item)
    x = inventoryfile.readline()
print("{:>20s}{:>20s}{:>20s}{:>20s}".format("Description","Units On Hand","Price","Inventory Value"))
for i in range(len(inventorylist)):
    print("{:>20s}{:>20d}{:>20.2f}{:>20.2f}".format(inventorylist[i].Description,inventorylist[i].UnitOnHand,inventorylist[i].Price,inventorylist[i].InventoryValue()))

updatedfile = open("11.01 InventoryUpdate.txt", "r")
updatedlist = []
y = updatedfile.readline()
while y !="":
    description, price = y.split(",")
    item = RetailItem(description, int(unit_on_hand), float(price))
    updatedlist.append(item)
    y = updatedfile.readline()
print("{:>20s}{:>20s}{:>20s}{:>20s}".format("Description","Units On Hand","Price","Inventory Value"))
for i in range(len(updatedlist)):
    print("{:>20s}{:>20d}{:>20.2f}{:>20.2f}".format(inventorylist[i].Description,inventorylist[i].UnitOnHand,updatedlist[i].Price,updatedlist[i].InventoryValue()))

updatedlist[find_inventory(updatedlist,"Inventory Value")]
print_updatedlist(updatedlist)