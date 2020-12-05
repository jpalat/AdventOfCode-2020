import unittest
from day41 import batchparser, passportValidator

class TestBatch(unittest.TestCase):
    
    def setUp(self):
        self.f = open('sample.txt','r')
    def tearDown(self):
        self.f.close()

    def test_batchExtractor(self):
        self.assertEqual(len(batchparser(self.f)), 4, "4 batches")

class TestValidation(unittest.TestCase):
    def test_validPassport(self):
        self.assertEqual(passportValidator({'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}), True, "Valid")
    def test_invalidPassport_missing_hgt(self):
        self.assertEqual(passportValidator({'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d', 'byr': '1929'}), False, "invalid")
    def test_invalidPassport_missing_cid(self):
        self.assertEqual(passportValidator({'hcl': '#ae17e1', 'iyr': '2013', 'eyr': '2024', 'ecl': 'brn', 'pid': '760753108', 'byr': '1931', 'hgt': '179cm'}), True, "Valid")
    def test_invalidPassport_missing_cid_byr(self):
        self.assertEqual(passportValidator({'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648', 'iyr': '2011', 'ecl': 'brn', 'hgt': '59in'}), False, "invalid")


if __name__ == "__main__":
    
    unittest.main()
