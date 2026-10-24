# String Methods Demo

A short Python script that demonstrates common string methods through practical examples: working with emails, names, phone numbers, addresses, and employee codes.

## What It Covers

| Topic | Methods Used |
|-------|--------------|
| Finding and slicing | `find()`, slicing (`[:n]`), `in` operator |
| Cleaning text | `strip()`, `lower()`, `title()`, `upper()` |
| Replacing text | `replace()` |
| Splitting and joining | `split()`, `join()` |
| Checking prefixes and suffixes | `startswith()`, `endswith()` |
| Counting | `count()` |

## Usage

Run the script from the command line:

```bash
python string_methods.py
```

No input is required and no external libraries are needed.

## Sections and Expected Output

### 1. Email analysis
Takes `alice.johnson@company.com` and:
- finds the position of `@` (`11`)
- extracts the username (`alice.johnson`)
- checks that the email contains `@` and `.com` (`True` for both)

### 2. Cleaning a messy name
`'  sARaH dAVis  '` becomes `'Sarah Davis'` using `strip()` and `title()`. The badge version, made with `upper()`, is `SARAH DAVIS`.

### 3. Cleaning a messy email
`'  SARAH.DAVIS@COMPANY.COM  '` becomes `sarah.davis@company.com` using `strip()` and `lower()`.

### 4. Username and display name
- Username: `sarah.davis`
- Display name: `Sarah Davis` (dots replaced with spaces, then title-cased)

### 5. Phone number
`123-456-7890` becomes `1234567890` by removing dashes with `replace()`.

### 6. Address splitting and joining
`'123 Main Street, Springfield, IL'` is split into a list:

```
['123 Main Street', 'Springfield', 'IL']
```

It is then rejoined as `123 Main Street | Springfield | IL`.

### 7. Employee code checks
For `EMP-2024-SD`:
- starts with `EMP`: `True`
- the cleaned email ends with `.com`: `True`

### 8. Counting characters
- Dots in `sarah.davis@company.com`: `2`
- Dashes in `EMP-2024-SD`: `2`

## Key Concepts

- **Slicing:** `email[:at_position]` returns everything before the `@`.
- **Method chaining:** `messy_name.strip().title()` applies several methods in a row.
- **Immutability:** string methods return a new string. The original is never changed.
- **Splitting and joining:** `split()` turns a string into a list, and `join()` turns a list back into a string.

## Requirements

- Python 3.6 or higher (uses f-strings)
