def reverse_string(A):
    reversed_str =""
    for char in A:
        reversed_str = char + reversed_str
    return reversed_str
def main():
    original_string = input("Enter a string:- ")
    reversed_string = reverse_string(original_string)
    print(f"original: {original_string}")
    print(f"reversed: {reversed_string}")

main()