# Railway Ticketing System

# Database
train_schedules = {
    "Train 1": {"source": "Delhi", "destination": "Mumbai", "seats": 100},
    "Train 2": {"source": "Mumbai", "destination": "Chennai", "seats": 150},
    "Train 3": {"source": "Chennai", "destination": "Delhi", "seats": 120}
}

tickets = {}

# Functions
def book_ticket(train_name, passenger_name):
    if train_name in train_schedules:
        if train_schedules[train_name]["seats"] > 0:
            ticket_id = len(tickets) + 1
            tickets[ticket_id] = {"train_name": train_name, "passenger_name": passenger_name}
            train_schedules[train_name]["seats"] -= 1
            print(f"Ticket booked successfully! Your ticket ID is {ticket_id}.")
        else:
            print("Sorry, no seats available on this train.")
    else:
        print("Invalid train name.")

def cancel_ticket(ticket_id):
    if ticket_id in tickets:
        train_name = tickets[ticket_id]["train_name"]
        train_schedules[train_name]["seats"] += 1
        del tickets[ticket_id]
        print("Ticket cancelled successfully.")
    else:
        print("Invalid ticket ID.")

def view_tickets():
    if tickets:
        print("Your tickets:")
        for ticket_id, ticket in tickets.items():
            print(f"Ticket ID: {ticket_id}, Train: {ticket['train_name']}, Passenger: {ticket['passenger_name']}")
    else:
        print("No tickets booked.")

# Main Program
while True:
    print("Railway Ticketing System")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. View Tickets")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        train_name = input("Enter train name: ")
        passenger_name = input("Enter passenger name: ")
        book_ticket(train_name, passenger_name)
    elif choice == "2":
        ticket_id = int(input("Enter ticket ID: "))
        cancel_ticket(ticket_id)
    elif choice == "3":
        view_tickets()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")