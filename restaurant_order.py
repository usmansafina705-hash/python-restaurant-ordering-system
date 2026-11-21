menu = {"Pasta": 120, "Pizza": 1700, "Coffee": 100, "Fruitchat": 100, "Burger": 120}

print("Welcome to Safina's Restaurant")
print("Here is our menu:")
print("Pizza: Rs1700\nPasta: Rs120\nBurger: Rs120\nFruitchat: Rs100\nCoffee: Rs100")

order_total = 0

print("What would you like to have?")
item1 = input("Please enter your first item: ")

if item1 in menu:
    order_total += menu[item1]
    print(f"Your item {item1} has been added to your order.")
else:
    print(f"Error: {item1} is not available.")

order_again = input("Do you want to order another item (Yes/No): ")

if order_again == "Yes":
    item2 = input("Please enter your next item: ")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Item {item2} has been added to your order.")
    else:
        print(f"Error: {item2} is not available.")
    another_item = input("Is there anything else you'd like to order (Yes/No): ")
    if another_item == "Yes":
        item3 = input("Please enter your next item: ")
        if item3 in menu:
            order_total += menu[item3]
            print(f"Item {item3} has been added to your order.")
        else:
            print(f"Error: {item3} is not available.")

print("Thanks for coming..")

print(f"The total amount you have to pay is {order_total}")

