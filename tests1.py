import unittest
from prime import is_prime

class Test(unittest.TestCase):
    def test_1(self):
        """Check that 1 is not a prime number"""
        self.assertFalse(is_prime(1))
    def test_2(self):
        """Check that 2 is not a prime number"""
        self.assertFalse(is_prime(2))
    def test_5(self):
        """Check that 5 is a prime number"""
        self.assertTrue(is_prime(5))
    def test_2(self):
        """Check that 25 in not a prime number"""
        self.assertFalse(is_prime(25))
if __name__ == "__main__":
    unittest.main()