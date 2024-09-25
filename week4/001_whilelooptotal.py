def total_user_number():
    total = 0
    number = float(input("Enter your number (0 to end)"))
    while number != 0:
        total += number
        number = int(input("Enter a number ( 0 to End):"))
    print("Total:", total)

def main():
    total_user_number()

main()