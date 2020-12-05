import unittest
from day41 import batchparser, passportValidator

class TestNavigator(unittest.TestCase):
    
    def setUp(self):
        self.f = open('sample.txt','r')
    def tearDown(self):
        self.f.close()

    def test_batchExtractor(self):
        self.assertEqual(len(batchparser(self.f)), 5, "5 batches")
    def test_validPassport(self):
        self.assertEqual(passportValidator([]), True, "Valid")
    def test_invalidPassport(self):
        self.assertEqual(passportValidator([]), False, "invalid")





if __name__ == "__main__":
    
    unittest.main()
    print("Trees Encountered", navigator(2,3))