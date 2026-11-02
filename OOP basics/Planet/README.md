# Planet Class Lab

A small Python project that models a planet using a class, with input validation, a custom string representation, and an `orbit` method.

## Features

- `Planet` class with `name`, `planet_type`, and `star` attributes
- Input validation in `__init__`:
  - Raises `TypeError` if any argument is not a string
  - Raises `ValueError` if any argument is an empty string
- `orbit()` method that describes the planet's orbit
- `__str__()` method for a readable string representation

## Usage

```python
planet = Planet('Earth', 'Terrestrial', 'Sun')

print(planet)
# Planet: Earth | Type: Terrestrial | Star: Sun

print(planet.orbit())
# Earth is orbiting around Sun...
```

## Error Handling

| Invalid input | Exception | Message |
|---|---|---|
| Any argument is not a string | `TypeError` | `name, planet type, and star must be strings` |
| Any argument is an empty string | `ValueError` | `name, planet_type, and star must be non-empty strings` |

```python
Planet(123, 'Terrestrial', 'Sun')   # TypeError
Planet('', 'Terrestrial', 'Sun')    # ValueError
```

## Running the Program

```bash
python planet.py
```

### Expected Output

```
Planet: Earth | Type: Terrestrial | Star: Sun
Planet: Jupiter | Type: Gas Giant | Star: Sun
Planet: Kepler-22b | Type: Super-Earth | Star: Kepler-22
Earth is orbiting around Sun...
Jupiter is orbiting around Sun...
Kepler-22b is orbiting around Kepler-22...
```

## Project Structure

```
.
├── planet.py   # Planet class and example instances
└── README.md   # Project documentation
```

## Concepts Covered

- Defining classes and instance attributes
- Raising built-in exceptions with custom messages
- Using `isinstance()` for type checking
- The `__str__` special method
- f-strings for formatting output
