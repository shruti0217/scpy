import unittest
import dashed

class TestString(unittest.TestCase): #create class Teststring which is inherited from  Testcase...
    def test_str(self):     # to check if the var passed to dashed() is of type string or not
       # self.assertTrue(dashed.var)
        self.assertIs(type(dashed.var),str) #ain't sure if this one is correct or not
    
    def test_result(self):      #Testing result with some other given strings
        self.assertEqual(dashed.dashed("Hello"),"H-e-ll-o-")
        self.assertEqual(dashed.dashed("Lost in the jungle"),"L-o-st -i-n th-e- j-u-ngl-e-")


if  __name__=="__main__":
    unittest.main()