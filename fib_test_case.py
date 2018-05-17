import unittest
from fibonanci import fib

class FibonanciTestCase(unittest.TestCase):
	def test_greater_than_2(self):
		self.assertEqual(fib(6), [0,1,1,2,3,5])		

	def test_less_than_2(self):
		self.assertEqual(fib(1), "1 is not greater than 2")

if __name__ == '__main__':
	unittest.main()
