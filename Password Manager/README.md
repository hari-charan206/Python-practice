Password Manager

A simple command-line Password Manager built using Python. The program allows users to add, view, search, and delete saved account credentials.
Features
* Add a new account
* View saved passwords
* Search for an account by website
* Delete an account
* Count saved accounts
* Simple menu-based interface

How It Works
The program stores account details using a list of dictionaries.
Each account contains:
* Website
* Username
* Password
The user can select an option from the menu to perform different operations.

Example
```text
==============================
       PASSWORD MANAGER
==============================
1. Add Password
2. View Passwords
3. Search Password
4. Delete Password
5. Count Passwords
6. Exit
==============================
Enter your choice: 1
--- Add Password ---
Enter website: github.com
Enter username: user123
Enter password: mypassword
Password saved successfully!
```
Concepts Used
* Variables
* Strings
* Lists
* Dictionaries
* Functions
* `if-elif-else`
* `for` loops
* `while` loops
* User input
* List methods
* Dictionary access

How to Run
Make sure Python is installed on your computer.

Run the following command:
```bash
python password_manager.py
```
Note
This is a beginner Python practice project. Passwords are stored in memory as plain text and are lost when the program exits. **Do not use this program to store real passwords.**

Future Improvements
* Add password encryption
* Generate strong passwords automatically
* Store data in a file or database
* Add password masking
* Add login authentication
