import unittest
from typing import List, Dict, Any
import json
from collections import defaultdict

def normalize_value(value: Any) -> Any:
    """
    Normalize a value for comparison by sorting dictionaries and lists (except lists of primitives).
    """
    if isinstance(value, dict):
        # Sort dictionary items by key and normalize their values
        return tuple(sorted((k, normalize_value(v)) for k, v in value.items()))
    elif isinstance(value, list):
        # Check if list contains only primitives
        if all(isinstance(x, (int, float, str, bool)) for x in value):
            return value  # Keep primitive lists as is
        # For non-primitive lists, sort after normalizing each element
        return tuple(sorted(normalize_value(x) for x in value))
    return value

def solve(input_dicts: List[Dict]) -> List[Dict]:
    """
    Deduplicate a list of dictionaries while respecting the order rules:
    - Lists of primitives maintain their order
    - Everything else is order-independent
    """
    seen = set()
    output = []
    
    for d in input_dicts:
        # Convert dict to normalized JSON string for comparison
        normalized = json.dumps(normalize_value(d), sort_keys=True)
        if normalized not in seen:
            seen.add(normalized)
            output.append(d)
    
    return output

class TestJsonDedupe(unittest.TestCase):
    def test_1_no_overlap(self):
        input = [
            {
                "Name": "John",
                "Age": 40
            },
            {
                "Name": "Nancy",
                "Age": 60,
            }
        ]
        output = solve(input)

        expected_output = [
            {
                "Name": "John",
                "Age": 40
            },
            {
                "Name": "Nancy",
                "Age": 60,
            }
        ]

        self.assertCountEqual(output, expected_output)

    def test_2_overlap(self):
        input = [
            {
                "Name": "John",
                "Age": 40
            },
            {
                "Name": "Nancy",
                "Age": 60,
            },
            {
                "Age": 40,
                "Name": "John",
            }
        ]
        output = solve(input)

        expected_output = [ 
            {
                "Name": "John",
                "Age": 40,
            },
            {
                "Name": "Nancy",
                "Age": 60,
            }
        ]

        self.assertCountEqual(output, expected_output)

    def test_3_nested_structures(self):
        input = [
            {"a": [{"x": 1}, {"y": 2}], "b": [0, 1]},
            {"b": [0, 1], "a": [{"y": 2}, {"x": 1}]},
            {"a": [{"x": 1}, {"y": 2}], "b": [0, 1]}
        ]
        output = solve(input)
        self.assertEqual(len(output), 1)

    def test_4_primitive_lists(self):
        input = [
            {"nums": [1, 0, 1]},
            {"nums": [0, 1, 1]},
            {"nums": [1, 0, 1]}
        ]
        output = solve(input)
        self.assertEqual(len(output), 2)  # [1,0,1] and [0,1,1] are different

    def test_5_empty_structures(self):
        input = [
            {"empty_list": [], "empty_dict": {}},
            {"empty_dict": {}, "empty_list": []},
            {"empty_list": [], "empty_dict": {}},
            {"a": []},
            {"a": []}
        ]
        output = solve(input)
        self.assertEqual(len(output), 2)  # One for empty structures, one for {"a": []}

    def test_6_mixed_types(self):
        input = [
            {"a": 1, "b": "string", "c": True, "d": 1.5},
            {"b": "string", "a": 1, "d": 1.5, "c": True},
            {"a": 1, "b": "string", "c": True, "d": 1.5}
        ]
        output = solve(input)
        self.assertEqual(len(output), 1)

if __name__ == "__main__":
    unittest.main() 