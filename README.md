# Restaurant_Menu
The provided code is a simple Python script that simulates a restaurant ordering system. Here’s a detailed breakdown of how it works:

▎Code Breakdown

1. Menu Definition:
      menu = {
       'Pizza': 60,
       'Pasta': 50,
       'Burger': 40,
       'Salad': 70,
       'Coffee': 80,
   }
   

   • A dictionary named menu is created, where the keys are the names of food items and the values are their respective prices.

2. Function Definition:
      def take_order():
   

   • The function take_order is defined to handle the ordering process.

3. Welcome Message:
      print("Welcome to Python Restaurant")
   print("Menu:")
   for item, price in menu.items():
       print(f"{item}: Rs{price}")
   

   • A welcome message is printed, followed by the menu items and their prices.

4. Order Total Initialization:
      order_total = 0
   

   • A variable order_total is initialized to keep track of the total cost of the order.

5. Order Loop:
      while True:
       item = input("Enter the name of the item you want to order (or type 'done' to finish) = ")
   

   • A while loop is initiated to allow continuous ordering until the user decides to finish.

6. Handling User Input:

   • The user is prompted to enter an item name or type 'done' to finish their order.

   • If the user types 'done', the loop breaks, and no more items can be ordered.

   
7. Adding Items to Order:
      if item in menu:
       order_total += menu[item]
       print(f"Your item {item} has been added to your order.")
   else:
       print(f"Order item {item} is not available yet!")
   

   • If the entered item exists in the menu, its price is added to order_total, and a confirmation message is printed.

   • If the item does not exist, an error message is displayed.

8. Prompt for Another Order:
      another_order = input("Do you want to add another item? (Yes/No) ")
   if another_order.lower() != "yes":
       break
   

   • After each valid order, the user is asked if they want to add another item. If they respond with anything other than "yes", the loop breaks.

9. Final Output:
      print(f"The total amount to pay is Rs{order_total}")
   

   • Once the user finishes ordering, the total amount due is printed.

10. Function Call:
        take_order()
    

    • The function take_order is called to initiate the ordering process when the script runs.

▎Summary

This script provides a straightforward command-line interface for customers to place orders at a restaurant. It allows users to select items from a predefined menu, calculates the total cost based on their selections, and provides feedback on their orders. 

▎Possible Enhancements

To improve this basic functionality, you might consider adding:

• Input validation for numeric entries (e.g., checking if the input is a valid menu item).

• Support for multiple quantities of each item.

• An option to view the current order before finalizing it.

• A feature to remove items from the order.

• A more structured output format for better readability.
