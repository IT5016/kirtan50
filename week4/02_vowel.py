def count_vowels(text):
    vowels ="aeiou"
    count = 0 

    for char in text:
        if char.lower() in vowels:
            count += 1
    return count
def main():
    text = input("Enter a string: ")
    print(f"Number of vowels in the string: {count_vowels(text)}")
main()
