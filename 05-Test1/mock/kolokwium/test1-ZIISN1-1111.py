'''
1. Place this program in the same folder as your programs.
2. To assess your programs, run this program.
3. Your results will be saved to the results.txt file.
'''

import sys
import unittest

class Test(unittest.TestCase):
    def test_p1(self):
        import p1
        self.assertEqual(p1.f(5),3)
        self.assertEqual(p1.f(9),21)
        self.assertEqual(p1.f(11),55)    
        self.assertEqual(p1.f(17),987)    

    def test_p2(self):
        import p2
        self.assertEqual(p2.f(987,1234567),True)
        self.assertEqual(p2.f(987,123456),False)

    def test_p3(self):
        import p3
        self.assertEqual(p3.f("super"),"s-uu-ppp-eeee-rrrrr")
        self.assertEqual(p3.f("screen"),"s-cc-rrr-eeee-eeeee-nnnnnn")

    def test_p4(self):
        import p4
        self.assertEqual(p4.f(-8),8)
        self.assertEqual(p4.f(8),-8)
        self.assertEqual(p4.f(-7),7)
        self.assertEqual(p4.f(7),7)

    def test_p5(self):
        import p5
        self.assertEqual(p5.f("abcdefgh","g",1),True)
        self.assertEqual(p5.f("bbcccddddcc","c",5),True)

    def test_p6(self):
        import p6
        self.assertEqual(p6.f(True,True,True,False),True)
        self.assertEqual(p6.f(True,True,True,True),True)
        self.assertEqual(p6.f(False,True,True,True),True)
        self.assertEqual(p6.f(True,True,False,False),False)


if __name__ == '__main__':
    sys.stderr = open('results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)
