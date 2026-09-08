Password Strength Checker

A simple Python program that checks whether a password is strong based on common password requirements.

Features
The program checks whether the password contains:
* At least 8 characters
* At least one uppercase letter
* At least one lowercase letter
* At least one digit
* At least one special character

How It Works
The program takes a password as input and checks each character using Python string methods.

| Requirement       | Python Method    |
| ----------------- | ---------------- |
| Minimum length    | `len()`          |
| Uppercase letter  | `.isupper()`     |
| Lowercase letter  | `.islower()`     |
| Digit             | `.isdigit()`     |
| Special character | `else` condition |

If all requirements are satisfied, the program displays:
```text
Strong Password
```

Otherwise, it displays:
```text
Weak Password
```

and tells the user which requirements are missing.
Example
Input
```text
Enter your password: Hello123
```

Output
```text
Weak Password
Password must contain a special character
```

Strong Password
```text
Enter your password: Hello@123
Strong Password
```

Concepts Practiced
* Variables
* Strings
* `if`, `elif`, and `else`
* `for` loops
* Boolean variables
* String methods
* `len()`
* Logical operators

Requirements
* Python 3.x

How to Run
1. Make sure Python is installed.
2. Save the program as:

```text
password_strength_checker.py
```

3. Run:
```bash
python password_strength_checker.py
```

Future Improvements
Possible improvements include:
* Checking for commonly used passwords
* Adding a password strength score
* Preventing repeated characters
* Adding password generation
* Creating a graphical user interface
