# Anagram Checker

## Description
A simple Python program that checks whether two words or phrases are anagrams of each other. Two words are anagrams if they contain the same letters in a different order.

## Features
- Accepts two words or phrases from the user.
- Ignores uppercase and lowercase differences.
- Ignores spaces.
- Checks whether both inputs contain the same letters.

## Example

```text
ANAGRAM CHECKER
Enter first word: listen
Enter second word: silent

They are anagrams!
```

## How It Works
1. Takes two inputs from the user.
2. Converts both inputs to lowercase.
3. Removes spaces.
4. Uses `sorted()` to arrange the letters alphabetically.
5. Compares both sorted results.
6. Displays whether they are anagrams.

## Concepts Used
- Functions
- Strings
- Conditional statements
- `sorted()` function
- String methods: `lower()` and `replace()`

## How to Run

```bash
python anagram_checker.py
```

## Future Improvements
- Ignore punctuation.
- Support complete sentences.
- Add repeated checking without restarting the program.

## Purpose
Created as a beginner Python project to practise string manipulation, functions, and conditional logic.
