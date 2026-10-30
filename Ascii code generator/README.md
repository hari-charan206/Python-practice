# ASCII Code Generator

A simple menu-based Python application that converts text into ASCII codes and ASCII codes back into readable text.

## Features

- Convert text into ASCII codes
- Convert ASCII codes into text
- Display the ASCII character table
- Find the ASCII value of an individual character
- Handle invalid inputs
- Interactive menu-based interface

## How It Works

The program uses Python's built-in functions:

- `ord()` – Converts a character into its ASCII integer value.
- `chr()` – Converts an integer into its corresponding character.
- `split()` – Separates input ASCII codes into individual values.
- `range()` – Generates numbers for displaying the ASCII table.

## Example

**Text to ASCII**

```text
Input: HELLO

H : 72
E : 69
L : 76
L : 76
O : 79
```

**ASCII to Text**

```text
Input: 72 69 76 76 79

Output: HELLO
```

## Concepts Used

- Variables and data types
- Functions
- Strings
- `for` and `while` loops
- Conditional statements
- Exception handling
- Type conversion
- Built-in functions (`ord()` and `chr()`)

## How to Run

Make sure Python is installed on your computer.

Run the following command:

```bash
python ascii_code_generator.py
```

## Limitations

This program supports standard ASCII values from 0 to 127. Extended ASCII and Unicode characters are not included.

## Future Improvements

- Add hexadecimal conversion
- Add binary conversion
- Add octal conversion
- Save conversion history
- Create a graphical user interface

## Purpose

This project was created to practice Python fundamentals, character encoding, string manipulation, and basic input validation.
