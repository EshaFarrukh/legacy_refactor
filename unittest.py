import unittest
import tempfile
import os
from legacy_refactor import read_numbers_from_file, compute_statistics

class TestStatisticsFunctions(unittest.TestCase):

    def test_compute_statistics_with_values(self):
        numbers = [10, 20, 30, 40]
        result = compute_statistics(numbers)
        self.assertEqual(result["total"], 4)
        self.assertEqual(result["sum"], 100)
        self.assertEqual(result["average"], 25)
        self.assertEqual(result["min"], 10)
        self.assertEqual(result["max"], 40)

    def test_compute_statistics_empty(self):
        result = compute_statistics([])
        self.assertEqual(result["total"], 0)
        self.assertEqual(result["sum"], 0)
        self.assertEqual(result["average"], 0)
        self.assertIsNone(result["min"])
        self.assertIsNone(result["max"])

    def test_read_numbers_from_file_valid(self):
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix=".txt") as temp_file:
            temp_file.write("5\n10\n15\n")
            temp_file_path = temp_file.name

        try:
            numbers = read_numbers_from_file(temp_file_path)
            self.assertEqual(numbers, [5, 10, 15])
        finally:
            os.remove(temp_file_path)

    def test_read_numbers_from_file_invalid(self):
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix=".txt") as temp_file:
            temp_file.write("10\nabc\n20\n")
            temp_file_path = temp_file.name

        try:
            with self.assertRaises(ValueError):
                read_numbers_from_file(temp_file_path)
        finally:
            os.remove(temp_file_path)

if __name__ == '__main__':
    unittest.main()
