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

class TestRules(unittest.TestCase):
    def setUp(self):
        self.floor = ['L','.','#'],['L','#','#'],['#','L','#']
        
    def testLR(self):
        self.assertEqual(check_left(0,1,self.floor), 0)
        self.assertEqual(check_left(1,2,self.floor), 1)
        self.assertEqual(check_left(0,0,self.floor), 0)
        self.assertEqual(check_left(0,1,self.floor), 0)
        self.assertEqual(check_right(0,1,self.floor), 1)
        self.assertEqual(check_right(1,2,self.floor), 0)
        self.assertEqual(check_right(0,0,self.floor), 0)    

    def testUD(self):
        self.assertEqual(check_up(0,1,self.floor), 0)
        self.assertEqual(check_up(1,1,self.floor), 0)
        self.assertEqual(check_up(1,2,self.floor), 1)
        self.assertEqual(check_down(0,1,self.floor), 1)
        self.assertEqual(check_down(2,2,self.floor), 0)
        self.assertEqual(check_down(0,0,self.floor), 0)
        self.assertEqual(check_down(0,1,self.floor), 1)
if __name__ == "__main__":
    unittest.main()
