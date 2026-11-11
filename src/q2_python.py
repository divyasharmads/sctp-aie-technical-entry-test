# Question 2 - Arrays and Loops
# Topic: Inventory Tracker
#
inventory = []

def addItem(itemName):
    if itemName in inventory:
        print(f"{itemName} is already in inventory.")
    else:
        inventory.append(itemName)

def listInventory():
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("Inventory:", inventory)


# Task 4:
# Call the functions in this order and observe the output:
addItem("Laptop")
addItem("Mouse")
addItem("Keyboard")
addItem("Mouse")   # Should trigger duplicate warning
listInventory()

# Expected output:
# Mouse is already in inventory.
# Inventory: ['Laptop', 'Mouse', 'Keyboard']
