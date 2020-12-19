import unittest
from day11 import *
class TestSeating(unittest.TestCase):
    
    def setUp(self):
        self.f = open('sample.txt','r')
    def tearDown(self):
        self.f.close()

    def test_find(self):
        data = list(self.f)
        self.assertEqual(model_seats(data),37)


if __name__ == "__main__":
    unittest.main()
