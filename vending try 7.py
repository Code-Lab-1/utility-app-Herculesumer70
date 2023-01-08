# Define a list of available snacks
snacks = [
    {
        "item": "break choclate",
        "code": "X01",
        "price": 2.00
    },
    {
        "item": "lays",
        "code": "X02",
        "price": 3.00
    },
    {
        "item": "water",
        "code": "X03",
        "price": 1.00
    },
    {
        "item": "pepsi",
        "code": "X04",
        "price": 2.50
    },
    {
        "item": "oman chips",
        "code": "X05",
        "price": 4.00
    },
    {
        "item": "doritos",
        "code": "X06",
        "price": 3.99
    },
    {
        "item": "twizzlers",
        "code": "X07",
        "price": 5.00
    },
    {
        "item": "best peanuts",
        "code": "X08",
        "price": 2.00
    },
    {
        "item": "tiffany chocolate wafers",
        "code": "X09",
        "price": 3.00
    },
    {
        "item": "galaxy chocolate",
        "code": "X10",
        "price": 2.50
    },
    {
        "item": "ritz",
        "code": "X11",
        "price": 3.50
    },
]

# Set up a flag to determine when the user has finished purchasing items
finish_purchasing = False

# Set up a variable to store the total amount of money inserted
total_amount = 0

# Set up a list to store the dispensed items
dispensed_items = []

# Set up a variable to store the total amount of change given
total_change = 0

# Set up a loop to run the vending machine
while not finish_purchasing:
    # Print a welcome message and the list of available snacks
    print("Welcome to your friendly vending machine")
    for i in snacks:
        print(f"Item {i['code']}: {i['item']} - Price: aed{i['price']}")

    # Prompt the user to select an item
    item_code = input("Please enter the code of the item you would like to purchase (or enter 'DONE' to finish purchasing): ")

    # If the user is finished purchasing, set the finish_purchasing flag to True
    if item_code.upper() == "DONE":
        finish_purchasing = True
        continue

    # Find the selected item in the list of available snacks
    item = None
    for i in snacks:
        if i["code"] == item_code:
            item = i
            break

    # If the item was not found, prompt the user to try again
    if item is None:
        print("Invalid item code. Please try again.")
        continue

    # Print the selected item and its price
    print(f"You have selected: {item['item']} - Price: aed{item['price']}")

    #
    # Prompt the user to insert money
    amount_inserted = float(input("Please insert money to purchase the item: "))

    # Calculate the change to give to the user
    change = amount_inserted - item["price"]

    # If the amount inserted is not enough to purchase the item, prompt the user to insert more money
    if change < 0:
        print(f"Insufficient funds. You need to insert aed{-change} more to purchase the item.")
        continue

    # Add the amount inserted to the total amount
    total_amount += amount_inserted

    # Add the change given to the total change
    total_change += change

    # Dispense the item and add it to the list of dispensed items
    print(f"Dispensing item: {item['item']}")
    dispensed_items.append(item["item"])

# Print a receipt with the list of dispensed items and the total change given
print("Thank you for using the vending machine!")
print("Here is your receipt:")
print("Dispensed items:")
for i in dispensed_items:
    print(i)
print(f"Total change: ${total_change:.2f}")
def dispense_item(item):
    # Code to dispense the item goes here
    print(f"Dispensing item: {item['item']}")
