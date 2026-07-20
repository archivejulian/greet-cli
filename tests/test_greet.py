import unittest

from greet import add_numbers, greet


class TestGreet(unittest.TestCase):
    def test_greet_returns_friendly_message(self):
        self.assertEqual(greet("world"), "Hello, world!")

    def test_greet_rejects_empty_name(self):
        with self.assertRaises(ValueError):
            greet("")


class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_numbers_with_negatives(self):
        self.assertEqual(add_numbers(-1, 1), 0)


if __name__ == "__main__":
    unittest.main()
