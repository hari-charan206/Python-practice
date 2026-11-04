# Email System Simulation

A simple object-oriented Python program that simulates an email system between users. Users can send emails, check their inbox, read messages, and delete them, all from the console.

## Features

- Send emails from one user to another
- Each user has their own inbox
- List inbox emails with a Read/Unread status
- Read a full email (automatically marks it as read)
- Delete emails by their inbox number
- Input checks for empty inboxes and invalid email numbers

## Project Structure

| File | Description |
|------|-------------|
| `email_system.py` | Contains all classes and the demo in `main()` |
| `README.md` | Project documentation |

## Classes

| Class | Responsibility |
|-------|----------------|
| `Email` | Stores sender, receiver, subject, body, timestamp and read status. Can mark itself as read and display its full content. |
| `User` | Represents a person with a name and an inbox. Provides `send_email`, `check_inbox`, `read_email` and `delete_email`. |
| `Inbox` | Holds a list of received emails. Handles listing, reading and deleting by 1-based index. |

## Requirements

- Python 3.6 or higher
- No external libraries (uses only the built-in `datetime` module)

## How to Run

```bash
python email_system.py
```

## Example Usage

```python
tory = User('Tory')
ramy = User('Ramy')

tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
ramy.check_inbox()      # list all emails
ramy.read_email(1)      # read email number 1
ramy.delete_email(1)    # delete email number 1
```

## Sample Output

```
Email sent from Tory to Ramy!

Email sent from Ramy to Tory!


Ramy's Inbox:

Your Emails:
1. [Unread] From: Tory | Subject: Hello | Time: 2026-11-04 10:30

--- Email ---
From: Tory
To: Ramy
Subject: Hello
Received: 2026-11-04 10:30
Body: Hi Ramy, just saying hello!
------------

Email deleted.


Ramy's Inbox:
Your inbox is empty.
```

> The timestamp will show the date and time at which you run the program.

## How It Works

1. `User.send_email()` creates an `Email` object and passes it to the receiver's `Inbox` via `receive_email()`.
2. `Inbox.list_emails()` prints each email using `Email.__str__()`, showing its Read/Unread status.
3. `Inbox.read_email(index)` finds the email and calls `display_full_email()`, which marks it as read.
4. `Inbox.delete_email(index)` removes the email from the list.

## Possible Improvements

- Sent folder for each user
- Search emails by sender or subject
- Save and load emails from a file or database
- Reply and forward features
- Unread email counter

## License

This project is free to use for learning and educational purposes.
