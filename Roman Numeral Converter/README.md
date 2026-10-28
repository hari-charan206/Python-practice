# Roman Numeral Converter

A Python command-line application that converts integers into Roman numerals and Roman numerals back into integers.

## Features

- Convert numbers to Roman numerals
- Convert Roman numerals to numbers
- Validate Roman numeral inputs
- Handle invalid inputs and characters
- Simple menu-based interface
- Support numbers from 1 to 3999

## Roman Numeral Symbols

| Symbol | Value |
|---|---:|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

## Examples

| Number | Roman numeral |
|---:|---|
| 4 | IV |
| 9 | IX |
| 14 | XIV |
| 49 | XLIX |
| 99 | XCIX |
| 2026 | MMXXVI |

## How It Works

The number-to-Roman function repeatedly subtracts the largest possible Roman numeral value until the number becomes zero.

The Roman-to-number function compares each symbol with the next one. If a symbol is smaller than the following symbol, its value is subtracted; otherwise, it is added.

The program also validates the result by converting it back into a Roman numeral and checking whether it matches the input.

## Concepts Used

- Variables and data types
- Functions and return values
- Lists and tuples
- Dictionaries
- `for` and `while` loops
- `if-else` conditions
- String manipulation
- Exception handling
- Input validation

## How to Run

Make sure Python is installed on your computer.

Run the following command in your terminal:

```bash
python roman_numeral_converter.py
```

## Limitations

The converter supports standard Roman numerals representing integers from 1 to 3999. Zero and negative numbers are not supported.

## Future Improvements

- Add a graphical user interface
- Add conversion history
- Support batch conversions
- Write automated unit tests

## Purpose

This project was created for Python practice and to improve problem-solving skills through string manipulation, loops, functions, and validation.
