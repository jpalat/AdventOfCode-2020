import unittest
from day9 import *
class TestDeclarations(unittest.TestCase):
    
    def setUp(self):
        self.f = open('sample.txt','r')
    def tearDown(self):
        self.f.close()

    def test_find(self):
        data = list(self.f)
        self.assertEqual(find(data, 5),127)

    def test_continuous(self):
        data = list(self.f)
        self.assertEqual(findContiguous(data, 127), [15,25,47,40])
    

if __name__ == "__main__":
    unittest.main()
