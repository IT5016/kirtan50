def get_shoppinglist():
    shopping_list = {}
    total_price = 0
    
    while True:
        item = input("Enter an item (or 'done' to finish): ")
        if item.lower() == "done":
            break
        try:
            price = float(input("Enter the price of the item: $"))
            shopping_list[item] = price
            total_price += price
        
        except ValueError:
            print("Invalid price entered. Please enter a numeric value.")
      
    
    return shopping_list,total_price
def main():
    print("Welcome to the Shopping List program")
    shopping_list, total_price = get_shoppinglist()
    
    if not shopping_list:
        print("No items added to the shopping list.")
        return
    else:
        print("\nShopping List:")
    for item, price in shopping_list.items():
        print(f"{item}: ${price:.2f}")
    print(f"Total Price: ${total_price:.2f}")
    
main()