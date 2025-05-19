# JSON Deduplication Tool

A Python utility for deduplicating JSON objects while respecting specific ordering rules.

## Features

- Deduplicates a list of JSON objects
- Maintains order for lists of primitive values (numbers, strings, booleans)
- Treats other structures (dictionaries, nested lists) as order-independent
- Includes comprehensive test suite

## Requirements

- Python 3.x

## Installation

No additional dependencies required. Simply clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

## Usage

### Running Tests

To run the test suite:

```bash
python json_dedupe.py
```

### Using in Your Code

```python
from json_dedupe import solve

# Example input with duplicates
input_dicts = [
    {"Name": "John", "Age": 40},
    {"Age": 40, "Name": "John"},  # This will be considered a duplicate
    {"Name": "Nancy", "Age": 60}
]

# Get deduplicated result
result = solve(input_dicts)
```

## Test Cases

The test suite includes several scenarios:

1. **Basic Deduplication**: Tests simple dictionary deduplication
2. **Nested Structures**: Handles complex nested JSON structures
3. **Primitive Lists**: Maintains order for lists of primitive values
4. **Empty Structures**: Handles empty lists and dictionaries
5. **Mixed Types**: Tests with various data types

## How It Works

The tool uses a normalization process to compare JSON objects:
1. Dictionaries are sorted by keys
2. Lists of primitives maintain their order
3. Other lists are sorted after normalization
4. The normalized form is used to identify duplicates

## Contributing

Feel free to submit issues and enhancement requests! 