import unittest
from day10 import chain
class TestDeclarations(unittest.TestCase):
    
    def setUp(self):
        self.f = open('sample1.txt','r')
    def tearDown(self):
        self.f.close()

    def test_chain(self):
        data = list(self.f)
        self.assertEqual(chain(data), {'1 jolt': 7, '3 jolts':5})

if __name__ == "__main__":
    unittest.main()