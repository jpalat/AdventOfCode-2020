import unittest
from day61 import getGroups

class TestDeclarations(unittest.TestCase):
    
    def setUp(self):
        self.f = open('sample.txt','r')
    def tearDown(self):
        self.f.close()

    def test_groups(self):
        self.assertEqual(len(getGroups(self.f)), 5, "5 groups found.")
    # def test_(self):
    #     self.assertEqual()

if __name__ == "__main__":
    unittest.main()
