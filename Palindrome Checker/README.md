# Palindrome Checker

A simple command-line Python program that checks whether a word or sentence reads the same forward and backward.

## Features

- Check words and sentences for palindromes
- Ignore uppercase and lowercase differences
- Ignore spaces and punctuation
- Simple menu-based interface
- Option to check multiple inputs

## How It Works

The program removes spaces and punctuation, converts the text to lowercase, and reverses the cleaned text. It then compares the original cleaned text with its reverse.

If both are equal, the input is a palindrome.

## Examples

| Input | Result |
|---|---|
| `madam` | Palindrome |
| `level` | Palindrome |
| `hello` | Not a palindrome |
| `A man, a plan, a canal: Panama` | Palindrome |

## Concepts Used

- Variables and strings
- Functions
- `for` and `while` loops
- `if-else` statements
- String methods: `lower()` and `isalnum()`
- String slicing: `[::-1]`
- User input and return values

## How to Run

Make sure Python is installed on your computer.

Run the following command:

```bash
python palindrome_checker.py
```

## Future Improvements

- Add palindrome checking for numbers
- Display the reversed text
- Count the number of characters
- Save previous results to a file

## Note

This project is intended for Python practice and learning fundamental programming concepts.
