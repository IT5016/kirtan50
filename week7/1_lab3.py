class RequestSystem:
    def __init__(self):
        self.request_id_counter = 1
        self.requests = []

    def user_info(self, name, age, email):
        user_details = {
            "name": name,
            "age": age,
            "email": email
        }
        return user_details

    def request_details(self, items):
        total_amount = 0
        request_items = []
        for item in items:
            total_amount += item["cost"]
            request_items.append(item)
        return total_amount, request_items

    def request_approval(self, total_amount):
        if total_amount < 150:
            return "approved"
        else:
            return "pending"

    def respond_request(self, request_id, status):
        for request in self.requests:
            if request["id"] == request_id:
                request["status"] = status
                break

    def display_request(self):
        for request in self.requests:
            print(f"Request ID: {request['id']}")
            print(f"Name: {request['user_details']['name']}")
            print(f"Total: ${request['total_amount']:.2f}")
            print(f"Status: {request['status']}")
            print("")

    def request_statistic(self):
        total_requests = len(self.requests)
        approved_requests = len([request for request in self.requests if request["status"] == "approved"])
        pending_requests = len([request for request in self.requests if request["status"] == "pending"])
        not_approved_requests = len([request for request in self.requests if request["status"] == "not approved"])
        print(f"Total number of requests submitted: {total_requests}")
        print(f"Total number of approved requests: {approved_requests}")
        print(f"Total number of pending requests: {pending_requests}")
        print(f"Total number of not approved requests: {not_approved_requests}")

    def submit_request(self, user_details, items):
        total_amount, request_items = self.request_details(items)
        status = self.request_approval(total_amount)
        request = {
            "id": self.request_id_counter,
            "user_details": user_details,
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
            print("3. Display Requests")
            print("4. Request Statistics")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("Enter your name: ")
                age = int(input("Enter your age: "))
                email = input("Enter your email: ")
                user_details = self.user_info(name, age, email)
                num_items = int(input("Enter the number of items: "))
                items = []
                for i in range(num_items):
                    item_name = input(f"Enter item {i+1} name: ")
                    item_cost = float(input(f"Enter item {i+1} cost: "))
                    item = {"name": item_name, "cost": item_cost}
                    items.append(item)
                self.submit_request(user_details, items)
            elif choice == "2":
                request_id = int(input("Enter the request ID: "))
                status = input("Enter the status (Approved/Not Approved): ")
                self.respond_request(request_id, status)
            elif choice == "3":
                self.display_request()
            elif choice == "4":
                self.request_statistic()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    request_system = RequestSystem()
    request_system.main()
    
    
    
    ##
    
#     class RequestSystem:
#     def _init_(self):
#         self.request_id_counter = 1
#         self.requests = []

#     def user_info(self, name, age, email):
#         return {"name": name, "age": age, "email": email}

#     def request_details(self, items):
#         total = sum(item["cost"] for item in items)
#         return {"total": total, "items": items}

#     def request_approval(self, total):
#         if total < 150:
#             return {"status": "approved", "reference": f"APR-{self.request_id_counter}"}
#         else:
#             return {"status": "pending", "reference": None}

#     def respond_request(self, request_id, status):
#         for request in self.requests:
#             if request["id"] == request_id:
#                 request["status"] = status
#                 if status == "approved":
#                     request["reference"] = f"APR-{request_id}"
#                 break

#     def display_request(self):
#         for request in self.requests:
#             print(f"Name: {request['user_info']['name']}")
#             print(f"Unique ID: {request['id']}")
#             print(f"Total: ${request['total']:.2f}")
#             print(f"Status: {request['status']}")
#             if request["status"] == "approved":
#                 print(f"Approval Reference: {request['reference']}")
#             print("")

#     def request_statistic(self):
#         total_requests = len(self.requests)
#         approved_requests = sum(1 for request in self.requests if request["status"] == "approved")
#         pending_requests = sum(1 for request in self.requests if request["status"] == "pending")
#         not_approved_requests = sum(1 for request in self.requests if request["status"] == "not approved")

#         print(f"Total number of requests submitted: {total_requests}")
#         print(f"Total number of approved requests: {approved_requests}")
#         print(f"Total number of pending requests: {pending_requests}")
#         print(f"Total number of not approved requests: {not_approved_requests}")

# def main():
#     request_system = RequestSystem()

#     while True:
#         print("1. Submit Request")
#         print("2. Respond to Request")
#         print("3. Display Requests")
#         print("4. Request Statistics")
#         print("5. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             name = input("Enter your name: ")
#             age = int(input("Enter your age: "))
#             email = input("Enter your email: ")
#             items = []
#             while True:
#                 item_name = input("Enter item name (or 'done' to finish): ")
#                 if item_name.lower() == "done":
#                     break
#                 item_cost = float(input("Enter item cost: "))
#                 items.append({"name": item_name, "cost": item_cost})

#             user_info = request_system.user_info(name, age, email)
#             request_details = request_system.request_details(items)
#             total = request_details["total"]
#             approval_response = request_system.request_approval(total)
#             request_system.requests.append({"id": request_system.request_id_counter, "user_info": user_info, "total": total, "items": items, "status": approval_response["status"], "reference": approval_response["reference"]})
#             request_system.request_id_counter += 1
#             print("Request submitted successfully!")

#         elif choice == "2":
#             request_id = int(input("Enter request ID: "))
#             status = input("Enter response (approved/not approved): ")
#             request_system.respond_request(request_id, status)
#             print("Request responded successfully!")

#         elif choice == "3":
#             request_system.display_request()

#         elif choice == "4":
#             request_system.request_statistic()

#         elif choice == "5":
#             break

#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "_main_":
#     main()