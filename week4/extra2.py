def calculate_amount():

    total_amount = 0.0
    
    while True:
        price_input = input("Enter the price of the item (or type 'finish' to end): ")
        
        if price_input.lower() == "finish":
            break
        try:
            price = float(price_input)
            total_amount += price
        except ValueError:
            print("Please enter a valid number or type 'finish' to end.")
            print(f"\nTotal Amount: ${total_amount:}")


calculate_amount()
