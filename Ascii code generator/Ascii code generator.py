def text_to_ascii(text):
    print("\n--- ASCII Codes ---")

    for char in text:
        print(char, ":", ord(char))


def ascii_to_text():
    print("\n--- ASCII to Text ---")

    numbers = input("Enter ASCII codes separated by spaces: ")

    try:
        codes = numbers.split()
        result = ""

        for code in codes:
            number = int(code)

            if 0 <= number <= 127:
                result += chr(number)
            else:
                print("Invalid ASCII code:", number)
                return

        print("Converted text:", result)

    except ValueError:
        print("Please enter valid numbers.")


def display_ascii_table():
    print("\n--- ASCII Table ---")

    for number in range(32, 127):
        print(number, ":", chr(number))


def find_ascii():
    print("\n--- Find ASCII Code ---")

    char = input("Enter a character: ")

    if len(char) == 1:
        print("ASCII Code:", ord(char))
    else:
        print("Please enter only one character.")


def main():
    while True:
        print("\n==============================")
        print("      ASCII CODE GENERATOR")
        print("==============================")
        print("1. Text to ASCII")
        print("2. ASCII to Text")
        print("3. Display ASCII Table")
        print("4. Find Character ASCII")
        print("5. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter text: ")
            text_to_ascii(text)

        elif choice == "2":
            ascii_to_text()

        elif choice == "3":
            display_ascii_table()

        elif choice == "4":
            find_ascii()

        elif choice == "5":
            print("Thank you for using ASCII Code Generator!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
