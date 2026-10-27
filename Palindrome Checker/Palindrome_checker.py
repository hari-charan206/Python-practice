def check_palindrome(text):
    cleaned_text = ""

    for char in text:
        if char.isalnum():
            cleaned_text += char.lower()

    reversed_text = cleaned_text[::-1]

    if cleaned_text == reversed_text:
        return True
    else:
        return False


def main():
    print("==========================")
    print("    PALINDROME CHECKER")
    print("==========================")

    while True:
        print("\n1. Check Palindrome")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter a word or sentence: ")

            if check_palindrome(text):
                print("It is a palindrome!")
            else:
                print("It is not a palindrome.")

        elif choice == "2":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
