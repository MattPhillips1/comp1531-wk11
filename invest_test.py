# code for the file investment_test.py
from investment import calculate_simple_interest, calculate_compound_interest
import unittest


# Create a new class that inherits from TestCase
class TestInvestment(unittest.TestCase):
    # Define initialisation tasks that are executed before the tests are run
    def setUp(self):
        self.principal = 1000
        self.interest = 5
        self.years = 5

    # Define the test-cases
    def test_function_calculate_simple_interest(self):
        self.assertEqual(
            calculate_simple_interest(
                self.principal,
                self.years, self.interest
            ), 250)

    def test_function_calculate_compound_interest(self):
        self.assertEqual(
            calculate_compound_interest(
                self.principal,
                self.years, self.interest
            ), 1276.2815625000003)

# Run the test-cases
if __name__ == '__main__':
    unittest.main()
