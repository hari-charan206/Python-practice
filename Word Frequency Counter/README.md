# Word Frequency Counter

## Description
A simple Python program that counts how many times each word appears in a sentence. It uses a dictionary to store each word and its frequency.

## Features
- Accepts a sentence from the user.
- Converts all words to lowercase.
- Counts the occurrences of each word.
- Ignores basic punctuation marks.
- Displays each word with its frequency.

## Example

```text
WORD FREQUENCY COUNTER
Enter a sentence: Python is easy and Python is fun

WORD FREQUENCY
python : 2
is : 2
easy : 1
and : 1
fun : 1
```

## How It Works
1. Takes a sentence as input.
2. Converts the sentence to lowercase.
3. Splits the sentence into individual words.
4. Uses a dictionary to store words and their counts.
5. Updates the count whenever a word appears again.
6. Displays the final word frequencies.

## Concepts Used
- Functions
- Dictionaries
- For loops
- Conditional statements
- String manipulation
- `split()`, `strip()`, `lower()`, and `get()` methods

## How to Run

```bash
python word_frequency_counter.py
```

## Future Improvements
- Display the most frequently used word.
- Sort words by frequency.
- Support reading text from files.
- Generate a frequency report.

## Purpose
Created as a beginner Python project to practise dictionaries, loops, functions, and string manipulation.
