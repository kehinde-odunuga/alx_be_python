import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
        
    def test_addition(self):
        self.assertEqual(self.calc.add(10, 2), 12)
        self.assertEqual(self.calc.add(-10, 2), -8)
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 2), 8)
        self.assertEqual(self.calc.subtract(-10, 2), -12)
        
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 2), 20)
        self.assertEqual(self.calc.multiply(-10, 2), -20)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, 0), None)
        

if __name__ == "__main__":
    unittest.main()