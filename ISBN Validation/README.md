# ISBN Validator

A simple Python command-line program that validates ISBN-10 and ISBN-13 codes by checking the final check digit against the one calculated from the main digits.

## How It Works

- **ISBN-10:** the first 9 digits are the main digits. The check digit is a number (0-9) or an uppercase `X`.
- **ISBN-13:** the first 12 digits are the main digits. The check digit is a number (0-9).
- The ISBN is valid only if the given check digit matches the calculated one.

## Usage

1. Uncomment the `main()` call at the bottom of the file.
2. Run the program:

   ```bash
   python isbn_validator.py
   ```

3. Enter the ISBN (without hyphens), a comma, and its length:

   ```
   Enter ISBN and length: 1530051126,10
   Valid ISBN Code.
   ```

## Example Inputs

| Input                | Output                                      |
|----------------------|---------------------------------------------|
| `1530051126,10`      | Valid ISBN Code.                            |
| `9971502100,10`      | Valid ISBN Code.                            |
| `080442957X,10`      | Valid ISBN Code.                            |
| `9781530051120,13`   | Valid ISBN Code.                            |
| `9781947172104,13`   | Valid ISBN Code.                            |
| `1530051125,10`      | Invalid ISBN Code.                          |
| `9781530051120,10`   | ISBN-10 code should be 10 digits long.      |
| `1530051126,13`      | ISBN-13 code should be 13 digits long.      |
| `15-0051126,10`      | Invalid character was found.                |
| `1530051126,9`       | Length should be 10 or 13.                  |
| `1530051125,A`       | Length must be a number.                    |
| `1530051125`         | Enter comma-separated values.               |

## Functions

- `validate_isbn(isbn, length)`: checks length, extracts main digits and check digit, and prints the result.
- `calculate_check_digit_10(main_digits_list)`: returns the expected ISBN-10 check digit as a string.
- `calculate_check_digit_13(main_digits_list)`: returns the expected ISBN-13 check digit as a string.
- `main()`: reads user input, handles input errors, and calls `validate_isbn`.

## Fixes Made

- Fixed the `IndentationError` in `main`.
- Handled `IndexError` for input that is not comma-separated.
- Handled `ValueError` for a non-numeric length.
- Fixed the off-by-one error: main digits are `isbn[:length - 1]` and the check digit is `isbn[length - 1]`.
- Handled `ValueError` for non-numeric characters in the main digits.
- Commented out the `main()` call so the tests can run.

## Requirements

- Python 3.6 or higher
