#!usr/bin/pyhton3.8.0
from unittest import TestCase
from unittest import main
from duplicate_ls import find_dup

class Testduplicate_ls(TestCase):

    @classmethod
    def setUpClass(cls):        #Testfixturecon
        cls.enviroment='testing'
    
    @classmethod 
    def tearDownClass(cls):
        pass

    def test_input_type(self):
        arr='a'
        
        self.assertRaises(AssertionError,find_dup,arr)


    def test_result(self):  
       in_arr=[3,2,4,3] #Sample input
       right_out=[3]    #expected output
       wrong_out=[3,3]  #Result should not have duplicate values
       out_Ac=find_dup(in_arr)   #Actual output

       self.assertNotEqual(out_Ac,wrong_out)

       self.assertEqual(out_Ac,right_out)
    
    def test_empty(self):
        arr=[]      
        self.assertRaises(AssertionError,find_dup,arr)
        
        



       
    

        
        


if __name__=="__main__":
    main()

