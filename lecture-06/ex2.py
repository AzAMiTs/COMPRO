inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]


def update_inventory(inv,item,qty):
    for itemn in inv:
        if itemn[0] == item:
            if itemn[1] >= qty:
                itemn[1] -= qty
            else:
                print("Not enough stack")
            return
    print("item not found!")
    
def calculate_total_value(inv):
    total = 0
    for item in inv:
        total += item[1] * item[2]
    return total


def find_most_expensive(inv):
    expensive = inv[0]
    for item in inv:
        if item[2] > expensive[2]:
            return expensive[0]
        

def add_item(inv,itemn,qty,price):
    for item in inv:
        if item[0] == itemn:
            item[1] = qty
            item[2] = price
            return
    inventory.append([itemn,qty,price])
update_inventory(inventory, "Banana", 20)

print("Total Inventory Value = $", calculate_total_value(inventory))

print("Most Expensive Item =", find_most_expensive(inventory))

add_item(inventory, "Eggs", 30, 0.25)

add_item(inventory, "Eggs", 50, 0.30)
    
    
print("\nFinal Inventory:")
for item in inventory:
    print(item)