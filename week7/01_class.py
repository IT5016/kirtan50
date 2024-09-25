
def staff_info(id_counters):
    print("Enter information:-")
    date = input("Date: ")
    name = input("Name: ")
    id = input("ID: ")

    unique_id =  id_counters + 1 
    id_counters = unique_id

    print("Enter date:" , date)
    print("Enter name:" , name)
    print("Enter ID:" , id)
    print("Requisition ID:", unique_id)

def main():
    id_counters = 10000
    staff_info(id_counters)
main()



