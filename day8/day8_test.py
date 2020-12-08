import unittest
from day8 import Bootloader

class TestBootloader(unittest.TestCase):

    def test_Parser(self):
        b = Bootloader('sample.txt')
        
        self.assertEqual(b.parseRule(0), ('nop', 0))
        self.assertEqual(b.parseRule(6), ('acc', -99))
        self.assertEqual(b.parseRule(8), ('jmp', -4))

    

    
    
    