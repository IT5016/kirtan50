# Railway Ticketing System

# Database =  store train schedules and available seats
train_schedules = {
    "Train 1": {"source": "Delhi", "destination": "Mumbai", "seats": 100},
    "Train 2": {"source": "Mumbai", "destination": "Chennai", "seats": 150},
    "Train 3": {"source": "Chennai", "destination": "Delhi", "seats": 120}
}
# Database: store booked tickets

tickets = {}

# Functions = book a ticket for a passenger on a specific train
def book_ticket(train_name, passenger_name):
     # Check if the train exists and has available seats
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

# Function: cancel a booked ticket
def cancel_ticket(ticket_id):
    # Check if the ticket ID exists
    if ticket_id in tickets:
        train_name = tickets[ticket_id]["train_name"]
        train_schedules[train_name]["seats"] += 1
        del tickets[ticket_id]
        print("Ticket cancelled successfully.")
    else:
        print("Invalid ticket ID.")

# Function: view all booked tickets
def view_tickets():
     # Check if there are any booked tickets
    if tickets:
        print("Your tickets:")
        for ticket_id, ticket in tickets.items():
            print(f"Ticket ID: {ticket_id}, Train: {ticket['train_name']}, Passenger: {ticket['passenger_name']}")
    else:
        print("No tickets booked.")

# Main Program: run the ticketing system

while True:
    print("Railway Ticketing System")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. View Tickets")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        # Book a ticket
        train_name = input("Enter train name: ")
        passenger_name = input("Enter passenger name: ")
        book_ticket(train_name, passenger_name)
    elif choice == "2":
        # Cancel a ticket
        ticket_id = int(input("Enter ticket ID: "))
        cancel_ticket(ticket_id)
    elif choice == "3":
        # View all booked tickets
        view_tickets()
    elif choice == "4":
        # Exit the program
        break
    else:
        print("Invalid choice. Please try again.")










Single Responsibility Principle (SRP)
Every function in the code should do no more but also no less than one thing.
This makes the code easier to maintain or modify, since now each function can change for only one reason.


Open-Closed Principle (OCP)
It should be open for extension and closed to modification.
For example, suppose we need to add a new feature of sending a confirmation email; we can add a new function without modifying the code that is already written.


Principle of Liskov Substitution (LSP)
This principle would be implemented whenever there is inheritance along with the use of polymorphism in our code.
It implies that subclass (say LuxuryTrain) must be able to replace its super class say, Train without affecting the correctness of the program.


Interface Segregation Principle (ISP)
This principle comes into play when we depend on interfaces within our code.
What that basically infers is that we must design an interface so that a client depends only on the interface they are using, without relying on methods that they do not use. 


Dependency Inversion Principle - DIP
This applies to high-level modules depending on low-level modules-for example, a PaymentGateway depending on a PaymentProcessor.
It means that the high-level module should depend on an interface instead of implementation, so that we could easily switch to other implementations without having to change the high-level module. 	

