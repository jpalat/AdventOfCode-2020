
import unittest
from day7 import parseRule

class TestLuggageRules(unittest.TestCase):
    def setUp(self):
        self.f = open('sample.txt','r')
    def tearDown(self):
        self.f.close()

    def test_ruleParser(self):
        self.assertEqual(parseRule('light red bags contain 1 bright white bag, 2 muted yellow bags.'), {'bright white':1, 'muted yellow':2})
        self.assertEqual(parseRule('faded blue bags contain no other bags.'), {})
        self.assertEqual(parseRule('bright white bags contain 1 shiny gold bag.'), {'shiny gold':1})


if __name__ == "__main__":
    unittest.main()
