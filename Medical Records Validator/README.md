Medical Records Validator

A Python program that validates the format and data types of medical records stored as dictionaries. It checks each record against predefined rules and reports invalid fields with their position in the records list.

Features
* Validates whether the input is a list or tuple.
* Checks whether each record is a dictionary.
* Verifies required dictionary keys.
* Validates patient ID and visit ID using regular expressions.
* Checks that age is an integer and at least 18.
* Validates gender values.
* Allows diagnosis to be a string or `None`.
* Checks that medications are stored as a list of strings.
* Reports the exact invalid field and its position.
* Returns `True` for valid data and `False` for invalid data.

Concepts Used
* Python dictionaries
* Lists and tuples
* Functions
* `for` loops
* `if` conditions
* List comprehensions
* `isinstance()`
* `enumerate()`
* `set`
* Regular expressions (`re`)
* `**kwargs` / dictionary unpacking

Example Output
For valid records:
```text
Valid format.
```

For invalid records:
```text
Unexpected format 'age: 15' at position 2.
```
How to Run
Make sure Python is installed, then run:
```bash
python medical_validator.py
```
Purpose
This project was created as a Python practice project to learn data validation, dictionaries, list comprehensions, regular expressions, and structured error handling.
