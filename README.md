# JSON Deduplication Tool

A Python utility for deduplicating JSON objects while respecting specific ordering rules.

## Features

- Deduplicates a list of JSON objects
- Maintains order for lists of primitive values (numbers, strings, booleans)
- Treats other structures (dictionaries, nested lists) as order-independent
- Includes comprehensive test suite
- Type hints for better IDE support

## Requirements

- Python 3.x
- typing-extensions (for enhanced type hints)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running Tests

To run the test suite:

```bash
python json_dedupe.py
```

### Using in Your Code

Basic usage:
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

Advanced usage with nested structures:
```python
from json_dedupe import solve

# Example with nested structures
input_dicts = [
    {
        "user": {
            "name": "John",
            "preferences": ["reading", "gaming"]
        },
        "scores": [1, 2, 3]
    },
    {
        "user": {
            "preferences": ["gaming", "reading"],
            "name": "John"
        },
        "scores": [1, 2, 3]
    }
]

# This will return only one item since the nested structures are considered equivalent
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

## Performance Considerations

- Time Complexity: O(n * m * log(m)) where:
  - n is the number of input dictionaries
  - m is the size of the largest dictionary
- Space Complexity: O(n * m) for storing the normalized forms
- Best for: Small to medium-sized JSON objects
- Consider using alternative solutions for very large datasets

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[Your Name/Organization]

## Acknowledgments

- Thanks to the Python community for the excellent typing support
- Inspired by the need for reliable JSON deduplication in data processing pipelines 