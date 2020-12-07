
import unittest
from day7 import parseRule

class TestLuggageRules(unittest.TestCase):
    def setUp(self):
        self.f = open('sample.txt','r')
    def tearDown(self):
        self.f.close()

    def test_ruleParser(self):
        self.assertEqual(parseRule('light red bags contain 1 bright white bag, 2 muted yellow bags.'), {'bright white bag':1, 'muted yellow bags':2})


if __name__ == "__main__":
    unittest.main()
