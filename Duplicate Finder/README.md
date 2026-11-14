# Duplicate Finder

## Description
A simple Python program that identifies duplicate elements in a list of numbers. It uses sets to track previously encountered elements and find duplicates.

## Features
- Accepts multiple numbers from the user.
- Identifies repeated elements.
- Displays each duplicate only once.
- Displays a message if no duplicates are found.

## Example

```text
DUPLICATE FINDER
Enter numbers separated by spaces: 10 20 30 20 40 10

Duplicate elements: ['10', '20']
```

## How It Works
1. Takes numbers as input from the user.
2. Splits the input into individual elements.
3. Creates two sets: `seen` and `duplicates`.
4. Checks whether each element has already appeared.
5. Adds repeated elements to the `duplicates` set.
6. Displays the duplicate elements.

## Concepts Used
- Functions
- Lists
- Sets
- For loops
- Conditional statements
- `sorted()` function

## How to Run

```bash
python duplicate_finder.py
```

## Future Improvements
- Support decimal numbers.
- Count how many times each element appears.
- Accept numbers from a text file.
- Display the total number of duplicates.

## Purpose
Created as a beginner Python project to practise lists, sets, loops, functions, and conditional logic.
