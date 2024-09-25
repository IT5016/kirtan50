
def collect_staff_information(id_requisition):                      
    print("Printing Staff Information: ")                      
    staff_id = input("Staff ID: ").strip()

    unique_id = id_requisition + 1
    id_requisition = unique_id

    Rstaff_id = staff_id + str(unique_id)[-3:]
    R_Number = Rstaff_id

    
    print(f"\nPrinting Staff Information:")
    print(f"Staff_id: {staff_id}" )
    print(f"Requisition ID: {id_requisition}")
   
    return id_requisition, unique_id,  staff_id, R_Number


def approve_requisition():
    # Define the conditions for approval
    items = []
    total_amount = 0.0
    while True:
        item_name = input("Enter Item Name and Price (Type 'finish' to end): ").strip()
        if item_name.lower() == 'finish':
            break
        try:
            name, price = item_name.rsplit(' ', 1)
            price = float(price.replace('$', ''))
            items.append((name, price))
            total_amount += price
        except ValueError:
            print("Invalid input. Please enter item name and price separated by a space.")

    return total_amount, items


def approval_request(total_amount):
    
    if total_amount < 500:
        Status = "Approved"
    elif total_amount < 1000:
        Status = "Review"
    else:
        Status = "Pending"

    return Status


# main
def main():
    id_requisition = 10000
    id_requisition, uniqe_id, staff_id, R_Number = collect_staff_information(id_requisition)
    total_amount, items = approve_requisition()
    Status = approval_request(total_amount)

    # Display the results
    print("\nOutput:")
    print(f"Total amount: ${total_amount:.2f}")
    print(f"status: {Status}")
    print(f"Approval Reference Number: {R_Number}")
   
if __name__ == "__main__":
    main()