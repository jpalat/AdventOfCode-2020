import unittest

from day51 import seatDecoder

class TestSeatDecoder(unittest.TestCase):
    def test_1(self):
        self.assertEqual(seatDecoder('FBFBBFFRLR'), (44, 5, 357))
        self.assertEqual(seatDecoder('BFFFBBFRRR'), (70, 7, 567))
        self.assertEqual(seatDecoder('FFFBBBFRRR'), (14, 7, 119))
        self.assertEqual(seatDecoder('BBFFBBFRLL'), (102, 4, 820))

if __name__ == "__main__":
    unittest.main()