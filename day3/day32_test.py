import unittest
from day32 import navigator

class TestNavigator(unittest.TestCase):
    
    def setUp(self):
        self.f = open('sample.txt','r')
    def tearDown(self):
        self.f.close()

    def test_11(self):
        self.assertEqual(navigator(self.f, 1 ,1), 2, "Should be 2")
    def test_13(self):
        self.assertEqual(navigator(self.f, 1 ,3), 7, "Should be 7")
    def test_15(self):
        self.assertEqual(navigator(self.f, 1 ,5), 3, "Should be 3")
    def test_17(self):
        self.assertEqual(navigator(self.f, 1 ,7), 4, "Should be 4")
    def test_21(self):
        self.assertEqual(navigator(self.f, 2 ,1), 2, "Should be 2")




if __name__ == "__main__":
    
    unittest.main()
    print("Trees Encountered", navigator(2,3))