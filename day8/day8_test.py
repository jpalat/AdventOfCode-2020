import unittest
from day8 import BootLoader

class TestBootloader(unittest.TestCase):

    def test_Parser(self):
        b = BootLoader('sample.txt')
        
        self.assertEqual(b.parseRule(0), ('nop', 0))
        self.assertEqual(b.parseRule(5), ('acc', -99))
        self.assertEqual(b.parseRule(7), ('jmp', -4))

    def test_Halt(self):
        b = BootLoader('sample.txt')
        self.assertEqual(b.execute(), 5)

    def test_unHalt(self):
        b = BootLoader('sample.txt')
        self.assertEqual(b.mutate(), 8)
    
if __name__ == "__main__":
    
    unittest.main()
    
    
    