# Kitchen Stock Manager

A short Python script that demonstrates functions, parameters, return values, and variable scope through a simple kitchen inventory example.

## What It Does

The script tracks three ingredients (eggs, flour, and sugar), prints the current stock, uses up eggs, and makes a fried egg only if enough eggs are available.

## Usage

```bash
python kitchen_stock.py
```

No input is required and no external libraries are needed.

## Functions

| Function | Purpose |
|----------|---------|
| `check_kitchen_stock()` | Prints the total item count and the amount of each ingredient, using the global variables. |
| `use_eggs(available_eggs, eggs_to_use)` | Checks whether there are enough eggs. If so, returns the remaining count. If not, prints a message and returns the original count. |
| `make_fried_egg(available_eggs)` | Uses one egg if at least one is available, prints a message, and returns the updated egg count. |

## Expected Output

```
The kitchen has 6 total items:
- 1 eggs
- 2 flour
- 3 sugar
1 egg(s) used out of 1 available.
1
1 egg(s) used out of 1 available.
Made a fried egg. Yummy!
The kitchen has 3 total items:
- 0 eggs
- 2 flour
- 3 sugar
```

## Key Concepts

- **Global vs. local variables:** The parameter `available_eggs` inside `use_eggs` and `make_fried_egg` is a local copy. Changing it does not change the global variable.
- **Return values matter:** The first call, `use_eggs(available_eggs, 1)`, returns the new count but the result is not saved. So `print(available_eggs)` still shows `1`.
- **Reassigning the result:** `available_eggs = make_fried_egg(available_eggs)` saves the returned value, so the global count is updated to `0`.
- **Guard conditions:** `use_eggs` checks `eggs_to_use > available_eggs` first, so the stock never goes negative.
- **Boolean variables:** `has_enough_eggs` stores a `True`/`False` result to make the `if` statement easy to read.

## Requirements

- Python 3.6 or higher (uses f-strings)
