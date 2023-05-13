import unittest
from mastermind import create_code 
from mastermind import check_correctness
from unittest.mock import patch
from io import StringIO
from mastermind import get_answer_input
from mastermind import take_turn
import sys

sys.stdout = StringIO()
class MyTestClass(unittest.TestCase):
    
    def test_create_code(self):
        '''Test that create_code function returns a list of4 digits that are:
            * in range 1 to 8 (8 is inclusive)
            * repeat 100 times
        '''

        for i in range(100):

            self.assertIsInstance(create_code(), list)
            self.assertEqual(len(create_code()), 4, 'The number of digits is not four')
            self.assertTrue(0 not in create_code() and 9 not in create_code(),
            'There is a zero or a 9 in your code')


    def test_check_correctness(self) :
        '''Test check_correct function that takes corect_digits_and_position,
        correct and turns as a parameters and returns a boolean True or False
        '''

        

        self.assertIsInstance(check_correctness(4,False, 10), bool, 'is not a list')
        self.assertEqual(check_correctness(4,False, 10),True)
        self.assertFalse(check_correctness(3,False,11))

        

    @patch("sys.stdin",StringIO("123\n12345\n1234\n"))
    def test_get_answer_input(self):
        '''Test get_user_input if it accepts 
        only four digits using patch as input
        '''
        
        self.assertEqual(get_answer_input(), "1234", 'number of digits is not four')
        
    
    @patch("sys.stdin",StringIO("12345\n2222\n1212\n1234\n"))
    def test_take_turn(self):
        ''' Test take turn which takes code as a parameter and 
            returns a tuple of correct digits in correct place and 
            correct digits not in correct place 
        '''
       
        self.assertEqual(take_turn([1,2,3,4]),(1,0))
        self.assertEqual(take_turn([1,2,3,4]),(2,0))
        self.assertEqual(take_turn([1,2,3,4]),(4,0))
        
        


if __name__ == '__main__' :
    unittest.main()
    