menu = {
    'Pizza': 60,
    'Pasta': 50,
    'Burger': 40,
    'Salad': 70,
    'Coffee': 80,
}

def take_order():
    print("Welcome to Python Restaurant")
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: Rs{price}")

    order_total = 0

    while True:
        item = input("Enter the name of the item you want to order (or type 'done' to finish) = ")
        
        if item.lower() == 'done':
            break
        
        if item in menu:
            order_total += menu[item]
            print(f"Your item {item} has been added to your order.")
        else:
            print(f"Order item {item} is not available yet!")

        another_order = input("Do you want to add another item? (Yes/No) ")
        if another_order.lower() != "yes":
            break

    print(f"The total amount to pay is Rs{order_total}")


take_order()