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
 
    def testTopDiag(self):
        self.assertEqual(check_tl(2, 2, self.floor), 1)
        self.assertEqual(check_tl(1, 2, self.floor), 0)
        self.assertEqual(check_tl(0, 2, self.floor), 0)
        self.assertEqual(check_tl(0, 0, self.floor), 0)
        self.assertEqual(check_tr(2, 1, self.floor), 1)
        self.assertEqual(check_tr(0, 1, self.floor), 0)
        self.assertEqual(check_tr(0, 1, self.floor), 0)
        self.assertEqual(check_tr(1, 2, self.floor), 0)


    def testBottomDiag(self):
        self.assertEqual(check_bl(0, 1, self.floor), 0)
        self.assertEqual(check_bl(0, 2, self.floor), 1)
        self.assertEqual(check_bl(2, 2, self.floor), 0)
        self.assertEqual(check_bl(0, 0, self.floor), 0)
        self.assertEqual(check_br(0, 0, self.floor), 1)
        self.assertEqual(check_br(1, 0, self.floor), 0)
        self.assertEqual(check_br(0, 2, self.floor), 0)
        self.assertEqual(check_br(2, 1, self.floor), 0)

    def testNeighbor_count(self):
        self.assertEqual(count_neighbors(1, 1, self.floor), 4)
        self.assertEqual(count_neighbors(0, 1, self.floor), 3)
        self.assertEqual(count_neighbors(2, 1, self.floor), 4)

class TestPt2Rules(unittest.TestCase):
    def setUp(self):
        self.full = open('sample_p21.txt','r')
        self.empty = open('sample_p22.txt','r')
    def tearDown(self):
        self.full.close()
        self.empty.close()

    def test_full(self):
        print('TEST Full')
        floor = list(self.full)
        floor_plan = []
        for l in floor:
            line = list(l.strip())
            floor_plan.append(line)
        print_floor(floor_plan)

        self.assertEqual(floor_plan[4][3] == 'L', True)
        self.assertEqual(count_neighbors2(4, 3, floor_plan), 8)
    
    def test_empty(self):
        print('TEST EMPTY')
        floor = list(self.empty)
        floor_plan = []
        for l in floor:
            line = list(l.strip())
            floor_plan.append(line)
        print_floor(floor_plan)

        self.assertEqual(floor_plan[3][3] == 'L', True)
        self.assertEqual(count_neighbors2(3, 3, floor_plan), 0)

    def test_examples(self):
        print("EXAMPLES")
        f = open('debug.txt','r')
        floor = list(f)
        floor_plan = []
        for l in floor:
            line = list(l.strip())
            floor_plan.append(line)
        f.close()
        self.assertEqual(count_neighbors2(0, 8 , floor_plan), 5)
        print('test2')
        self.assertEqual(count_neighbors2(1, 9 , floor_plan), 5)

    def testMutate2(self):
        print("Mutate2")
        f = open('sample.txt','r')
        self.assertEqual(model_seats2(f), 26)
        f.close()
if __name__ == "__main__":
    unittest.main()
