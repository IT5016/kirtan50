id = 5000

def collect_user_data(counter):

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    user_id = counter + 1
    
    print(f"\nUser Information:\nID: {user_id}\nName: {name}\nAge: {age}\nEmail: {email}")
    return user_id, counter + 1


id, new = collect_user_data(id)
