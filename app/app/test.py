"""
Sample tests

This file demonstrates how to write and run tests in Python using Django's
test framework.

How Python and Django Tests Work:
- Python's built-in `unittest` framework is used by Django for testing.
- Test cases are written as classes that inherit from
  `django.test.SimpleTestCase` or `django.test.TestCase`.
- Each test method should start with `test_` and will be automatically
  discovered and run by Django's test runner.
- To run all tests, use the command: `python manage.py test`
- Assertions (like `self.assertEqual`) are used to check that code behaves
  as expected.

In this file:
- We test functions from the `calc` module (add and subtract).
- Each test checks that the function returns the correct result for given
  inputs.
"""


from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        res = calc.add(8, 4)
        self.assertEqual(res, 12)

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted from each other"""
        res = calc.subtract(8, 16)
        self.assertEqual(res, -8)
