class Retail_Item:
    def __init__(self, Description = "", UnitsOnHand = 0, Price = 0):   
        self.Description = Description
        self.UnitsOnHand = UnitsOnHand
        self.Price = Price
    
    def Inventory_Value(self):       
        return self.UnitsOnHand * self.Price

def to_print_inventory(inventory_list):       
    print("Description\tUnits On Hand\tPrice\tInventory Value")    
    for elem in inventory_list:                                   
        obj = Retail_Item(elem[0], int(elem[1]), float(elem[2]))      
        print("{:>11}\t{:>13}\t{:>5}\t{:>15.2f}".format(elem[0], elem[1], elem[2], obj.Inventory_Value()))

def to_find_inventory(inventory_list, Description):   
    for i in range(len(inventory_list)):
        if (inventory_list[i][0] == Description):
            return i
    return -1

def main():                         
    inventory_list = []             
    filepath = "11.01 Inventory.txt"
    
    with open(filepath) as fp:
        while True:
            text = fp.readline().strip()
            if not text:
                break
            
            inventory_list.append(text.split(", "))

    to_print_inventory(inventory_list) 
    print("\n")

    inventory_update_list = []         
    filepath1 = "11.01 InventoryUpdate.txt"   
    with open(filepath1) as fp1:
        while True:
            text = fp1.readline().strip()
            if not text:
                break
    
            inventory_update_list.append(text.split(", "))

    for elem in inventory_update_list:
        pos = to_find_inventory(inventory_list, elem[0])
        if (pos != -1):
            inventory_list[pos][2] = elem[1]
    
    to_print_inventory(inventory_list)      
        
if __name__ == "__main__":
    main()      