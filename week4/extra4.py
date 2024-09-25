def create_detailed_report(name, total_amount, category, recommendation):

    print(f"User's Name: {name}")
    print(f"Total Amount: ${total_amount:.2f}")
    print(f"Category: {category}")
    print(f"Recommendation: {recommendation}")

def categorize_request(total_amount):

    if total_amount < 500:
        category = "Low"
        recommendation = "Proceed with standard processing."
    else:
        category = "High"
        recommendation = "Review for potential discounts."
    
    return category, recommendation

def calculate_total_amount():
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
    
    print(f"\nTotal Amount: ${total_amount:.2f}")
    return total_amount

def collect_user_data(counter):

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    
    user_id = counter + 1
    
    print(f"\nUser Information:\nID: {user_id}\nName: {name}\nAge: {age}\nEmail: {email}")
    return name, user_id, counter + 1

id_counter = 5000
name, user_id, id_counter = collect_user_data(id_counter)
total_amount = calculate_total_amount()
category, recommendation = categorize_request(total_amount)
create_detailed_report(name, total_amount, category, recommendation)
