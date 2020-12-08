
import unittest
from day7 import parseRule, validate

class TestLuggageRules(unittest.TestCase):
    def setUp(self):
        self.f = open('sample.txt','r')
    def tearDown(self):
        self.f.close()

    def test_ruleParser(self):
        self.assertEqual(parseRule('light red bags contain 1 bright white bag, 2 muted yellow bags.'), {'light red': {'bright white':1, 'muted yellow':2}})
        self.assertEqual(parseRule('faded blue bags contain no other bags.'), {'faded blue':{}})
        self.assertEqual(parseRule('bright white bags contain 1 shiny gold bag.'), {'bright white': {'shiny gold':1}})

    def test_Query(self):
        rules = list(self.f)
        self.assertEqual(validate(rules, 'shiny gold'), 4)


if __name__ == "__main__":
    unittest.main()
