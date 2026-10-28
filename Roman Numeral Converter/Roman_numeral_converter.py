def number_to_roman(number):
    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = ""

    for value, symbol in values:
        while number >= value:
            result += symbol
            number -= value

    return result


def roman_to_number(roman):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    roman = roman.upper()
    total = 0

    for i in range(len(roman)):
        current = values[roman[i]]

        if i + 1 < len(roman):
            next_value = values[roman[i + 1]]

            if current < next_value:
                total -= current
            else:
                total += current
        else:
            total += current

    # Check whether the input is a valid Roman numeral.
    if 1 <= total <= 3999:
        if number_to_roman(total) == roman:
            return total

    return None


def main():
    while True:
        print("\n==============================")
        print("   ROMAN NUMERAL CONVERTER")
        print("==============================")
        print("1. Number to Roman Numeral")
        print("2. Roman Numeral to Number")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                number = int(input("Enter a number (1-3999): "))

                if 1 <= number <= 3999:
                    print("Roman numeral:", number_to_roman(number))
                else:
                    print("Please enter a number from 1 to 3999.")

            except ValueError:
                print("Invalid input. Please enter a whole number.")

        elif choice == "2":
            roman = input("Enter a Roman numeral: ").strip()

            if not roman:
                print("Please enter a Roman numeral.")
                continue

            if all(char in "IVXLCDMivxlcdm" for char in roman):
                result = roman_to_number(roman)

                if result is not None:
                    print("Number:", result)
                else:
                    print("Invalid Roman numeral.")
            else:
                print("Invalid characters in Roman numeral.")

        elif choice == "3":
            print("Thank you for using the converter!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
