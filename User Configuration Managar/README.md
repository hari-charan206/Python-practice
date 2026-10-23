# User Configuration Manager

A small Python program for managing user settings such as theme, language, and notifications. Settings are stored in a dictionary, and four functions let you add, update, delete, and view them.

## Features

- **Add** a new setting (rejects duplicates)
- **Update** the value of an existing setting
- **Delete** a setting
- **View** all settings in a formatted list
- Keys and values are stored in **lowercase**, so `THEME` and `theme` are treated as the same setting

## Requirements

- Python 3.6 or higher (uses f-strings)
- No external libraries

## Usage

Run the program with:

```bash
python main.py
```

Or import the functions into your own code:

```python
from main import add_setting, update_setting, delete_setting, view_settings

settings = {'theme': 'light', 'language': 'english'}

print(add_setting(settings, ('Volume', 'High')))
print(update_setting(settings, ('theme', 'dark')))
print(delete_setting(settings, 'language'))
print(view_settings(settings))
```

## Functions

| Function | Parameters | Description |
|---|---|---|
| `add_setting` | `settings` (dict), `tuplee` (key, value) | Adds a new setting. Returns an error message if the key already exists. |
| `update_setting` | `settings` (dict), `tuplee` (key, value) | Updates an existing setting. Returns an error message if the key doesn't exist. |
| `delete_setting` | `settings` (dict), `key` (str) | Removes a setting. Returns `Setting not found!` if the key doesn't exist. |
| `view_settings` | `settings` (dict) | Returns all settings as a formatted string, or `No settings available.` if empty. |

## Example Output

```
Setting 'theme' already exists! Cannot add a new setting with this name.
Setting 'volume' added with value 'high' successfully!
Setting 'theme' updated to 'dark' successfully!
Setting 'brightness' does not exist! Cannot update a non-existing setting.
Setting 'language' deleted successfully!
Current User Settings:
Theme: dark
Volume: high
```

## Behavior Notes

- Keys and values are converted to lowercase before any check or storage.
- Return messages show the lowercase key and value.
- `view_settings` capitalizes each key for display, puts each setting on its own line, and ends with a trailing newline.
- All functions modify the dictionary passed in (they don't make a copy).

## Project Structure

```
.
├── main.py      # Setting management functions and test calls
└── README.md
```
