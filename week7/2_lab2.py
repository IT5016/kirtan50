class MembershipSystem:
    def __init__(self):
        self.members = []
        self.registered_members = 0
        self.withdrawn_members = 0
        self.diploma_students = 0
        self.bachelor_students = 0

    def register_member(self, student_id, last_name, programme):
        if programme not in ["Diploma", "Bachelor"]:
            print("Invalid programme. Please enter 'Diploma' or 'Bachelor'.")
            return
        membership_id = len(self.members) + 1
        self.members.append({
            "Student ID": student_id,
            "Last Name": last_name,
            "Programme": programme,
            "Membership ID": membership_id
        })
        self.registered_members += 1
        if programme == "Diploma":
            self.diploma_students += 1
        else:
            self.bachelor_students += 1
        print(f"Member {last_name} with ID {student_id} has been registered successfully.")

    def withdraw_member(self, membership_id, last_name):
        for member in self.members:
            if member["Membership ID"] == membership_id and member["Last Name"] == last_name:
                self.members.remove(member)
                self.registered_members -= 1
                self.withdrawn_members += 1
                print(f"Member {last_name} with ID {membership_id} has withdrawn successfully.")
                return
        print("Member not found.")

    def display_members(self):
        print("Membership Registration System")
        print("-------------------------------")
        print(f"Registered Members: {self.registered_members}")
        print(f"Diploma Students: {self.diploma_students}")
        print(f"Bachelor Students: {self.bachelor_students}")
        print(f"Withdrawn Members: {self.withdrawn_members}")
        print("-------------------------------")
        for member in self.members:
            print(f"Membership ID: {member['Membership ID']}, Student ID: {member['Student ID']}, Last Name: {member['Last Name']}, Programme: {member['Programme']}")

# Create an instance of the MembershipSystem class
system = MembershipSystem()

# Register some members
system.register_member("S123456", "John", "Diploma")
system.register_member("S789012", "Jane", "Bachelor")
system.register_member("S345678", "Bob", "Diploma")

# Display registered members
system.display_members()

# Withdraw a member
system.withdraw_member(1, "John")

# Display updated members
system.display_members()