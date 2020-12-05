import unittest
from day42 import batchparser, passportValidator, fieldValidator

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

class TestFieldValidation(unittest.TestCase):
    def test_byr_valid(self):
        self.assertEqual(fieldValidator('byr','2002'), True, 'Valid')
    def test_byr_invalid(self):
        self.assertEqual(fieldValidator('byr','2003'), False, 'Invalid')
    def test_iyr_valid(self):
        self.assertEqual(fieldValidator('iyr','2011'), True, 'Valid')
    def test_iyr_invalid(self):
        self.assertEqual(fieldValidator('iyr','2003'), False, 'Invalid')
    def test_hgt_valid_in(self):
        self.assertEqual(fieldValidator('hgt','60in'), True, 'Valid')
    def test_hgt_valid_cm(self):
        self.assertEqual(fieldValidator('hgt','190cm'), True, 'Valid')
    def test_hgt_invalid_measure(self):
        self.assertEqual(fieldValidator('hgt','190in'), False, 'Invalid')
    def test_hgt_invalid_units(self):
        self.assertEqual(fieldValidator('hgt','190'), False, 'Invalid')
    def test_hcl_valid(self):
        self.assertEqual(fieldValidator('hcl','#123abc'), True, 'Valid')
    def test_hcl_invalid_value(self):
        self.assertEqual(fieldValidator('hcl','#123abz'), False, 'Invalid')
    def test_hcl_invalid_ha(self):
        self.assertEqual(fieldValidator('hcl','123abc'), False, 'Invalid')
    def test_ecl_valid(self):
        self.assertEqual(fieldValidator('ecl','brn'), True, 'Valid')
    def test_ecl_invalid(self):
        self.assertEqual(fieldValidator('ecl','wat'), False, 'Invalid')
    def test_pid_valid(self):
        self.assertEqual(fieldValidator('pid','000000001'), True, 'Valid')
    def test_pid_invalid(self):
        self.assertEqual(fieldValidator('pid','0123456789'), False, 'Invalid')
    def test_pid_invalid_nn(self):
        self.assertEqual(fieldValidator('pid','012E5678'), False, 'Invalid')
 
if __name__ == "__main__":
    
    unittest.main()
