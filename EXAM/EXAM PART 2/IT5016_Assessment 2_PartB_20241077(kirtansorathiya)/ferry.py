class BookingSystem:
    def __init__(self):
        self.request_id_counter = 20000
        self.requests = []  
        
    def customer_info(self, id_number, name, status):
        customer_details = {
            "id_number": id_number,
            "name":  name,
            "status":  status,
        }
        return customer_details
    
    def ferry_service_details(self, items):
        total_amount = 0
        ferry_service_details = []
        for item in items:  
            total_amount += item["cost"]
            ferry_service_details.append(item)
        return total_amount,  ferry_service_details
    
    def booking_approval(self, total_amount):
        if total_amount < 150:
            return "approved"
        else:
            return "pending"
        
        
    def respond_request(self, request_id, status):
        for request in self.requests:
            if request["id"] == request_id:
                request["status"] = status
                break
    
    def display_booking_info(self):
        for request in self.requests:
            print(f"ID number: {request['passenger_details']['id_number']}")
            print(f"Name: {request['passenger_details']['name']}")
            print(f"Total: ${request['total_amount']:.2f}")
            print(f"Status: {request['status']}")
            
    def booking_statistic(self):
        total_requests = len(self.requests)
        approved_requests = len([request for request in self.requests if request["status"] == "approved"])
        pending_requests = len([request for request in self.requests if request["status"] == "pending"])
        not_approved_requests = len([request for request in self.requests if request["status"] == "not approved"])
        print(f"The Total number of bookings submitted: {total_requests}")
        print(f"The total number of approved bookings: {approved_requests}")
        print(f"The total number of pending bookings: {pending_requests}")
        print(f"The total number of not approved bookings: {not_approved_requests}")
        
    def submit_request(self, passenger_details, items):
        total_amount, request_items = self.ferry_service_details(items)  
        status = self.booking_approval(total_amount)
        request = {
            "id": self.request_id_counter,
            "passenger_details": passenger_details,
            "items": request_items,
            "total_amount": total_amount,
            "status": status
        }
        self.requests.append(request)
        self.request_id_counter += 1

    def main(self):
        while True:
            print("1. Submit Request")  
            print("2. Respond to Request")  
            print("3. Display Booking")
            print("4. Booking Statistics")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                Form_of_id = input("Enter your form of id: ")
                ID_number = input("Enter your ID number: ")
                Passenger_name = input("Enter your Passenger Name: ")
                passenger_details = self.customer_info(Form_of_id, ID_number, Passenger_name)
                num_items = int(input("Enter the number of items: "))
                items = []
                for i in range(num_items):
                    item_name = input(f"Enter item {i+1} name: ")
                    item_cost = int(input(f"Enter item {i+1} cost: "))
                    item = {"name": item_name, "cost": item_cost}
                    items.append(item)
                self.submit_request(passenger_details, items)
            elif choice == "2":
                request_id = int(input("Enter the request ID: "))
                status = input("Enter the status (Approved/Not Approved): ")
                self.respond_request(request_id, status)
            elif choice == "3":
                self.display_booking_info()
            elif choice == "4":
                self.booking_statistic()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    request_system = BookingSystem()
    request_system.main()