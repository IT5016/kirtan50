
def collect_staff_information(id_requisition):                     
    print("Printing Staff Information: ")
    staff_name = input("Staff Name: ").strip()                     
    staff_id = input("Staff ID: ").strip()
    date = input("Date: ").strip()  

    uniqe_id = id_requisition + 1
    id_requisition = uniqe_id

    Rstaff_id = staff_id + str(uniqe_id)[-3]
    R_Number = Rstaff_id

    
    print(f"\nPrinting Staff Information:")
    print(f"Staff Name: {staff_name}")
    print(f"Staff_id: {staff_id}" )
    print(f"Date: {date}")
    print(f"Requisition ID: {id_requisition}")
    
    return id_requisition, uniqe_id, staff_name, staff_id, date, R_Number




def requisitions_total():

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
    id_requisition, uniqe_id, staff_name, staff_id, date, R_Number = collect_staff_information(id_requisition)
    total_amount, items = requisitions_total()
    Status = approval_request(total_amount)

    # Display the results
    print("\nPrinting Requisitions:")
    print(f"Date: {date}")
    print(f"Requisition ID: {id_requisition}")
    print(f"Staff_id: {staff_id}" )
    print(f"Staff Name: {staff_name}")
    print(f"Total amount: ${total_amount:.2f}")
    print(f"status: {Status}")
    print(f"Approval Reference Number: {R_Number}")
   
if __name__ == "__main__":
    main()