import unittest
class TestChain(unittest.TestCase):
    

    def test_chain(self):
        self.f = open('sample1.txt','r')
        data = list(self.f)
        self.f.close()
        self.assertEqual(chain(data), {'1 jolt': 7, '3 jolts':5})
    def test_chain2(self):
        self.f = open('sample2.txt','r')
        data = list(self.f)
        self.f.close()
        self.assertEqual(chain(data), {'1 jolt': 22, '3 jolts':10})

if __name__ == "__main__":
    unittest.main()