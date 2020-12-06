import unittest
from day61 import getGroups

class TestDeclarations(unittest.TestCase):
    
    def setUp(self):
        self.f = open('sample.txt','r')
    def tearDown(self):
        self.f.close()

    def test_groups(self):
        self.assertEqual(len(getGroups(self.f)), 5, "5 groups found.")
    def test_batch_contents(self):
        groups = getGroups(self.f)
        self.assertEqual(groups[0], ['abc'])
        self.assertEqual(groups[1], ['a','b','c'])
        self.assertEqual(groups[3], ['a','a','a','a'])

    # def test_(self):
    #     self.assertEqual()


if __name__ == "__main__":
    unittest.main()
