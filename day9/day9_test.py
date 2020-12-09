import unittest
from day9 import find
class TestDeclarations(unittest.TestCase):
    
    def setUp(self):
        self.f = open('sample.txt','r')
    def tearDown(self):
        self.f.close()

    def test_find(self):
        data = list(self.f)
        self.assertEqual(find(data, 5),127)
   

if __name__ == "__main__":
    unittest.main()
