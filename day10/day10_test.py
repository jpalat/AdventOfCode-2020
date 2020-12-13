import unittest
from day10 import chain
class TestDeclarations(unittest.TestCase):
    

    def test_chain(self):
        self.f = open('sample1.txt','r')
        data = list(self.f)
        self.f.close()
        self.assertEqual(chain(data), {'1 jolt': 7, '3 jolts':5})

if __name__ == "__main__":
    unittest.main()