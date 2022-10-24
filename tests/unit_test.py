import unittest
import random
import numpy as np
import sys
sys.path.append('../')
import data_processor as dp  # nopep8

class TestUtils(unittest.TestCase):

    # ***Test get_random_matrix***
    def test_error_get_random_matrix(self):
        # TypeError if input not integer
        self.assertRaises(TypeError, dp.get_random_matrix, 2.5, 4)
        self.assertRaises(TypeError, dp.get_random_matrix, 3, 'a')

        # IndexError if either input < 1
        self.assertRaises(IndexError, dp.get_random_matrix, 0, 0)

    def test_fixed_get_random_matrix(self):
        test = np.array([[0.5, 0.5, 0.5],
                          [0.7, 0.7, 0.7]])
        real = dp.get_random_matrix(2, 3)
        
        # positve test
        self.assertEqual(test.shape, real.shape)
        
        # values >= 0
        self.assertGreaterEqual(min(real), 0)
        
        # values <= 1
        self.assertLessEqual(max(real), 1)
        
        # negative test
        self.assertEqual((1,1),real.shape)
                         
    def test_random_get_random_matrix(self):
        a = random.randint(1,10)
        b = random.randint(1,10)
        real = dp.get_random_matrix(a,b)
        
        # positve test
        self.assertEqual((a,b), real.shape)
        
        # values >= 0
        self.assertGreaterEqual(min(real), 0)
        
        # values <= 1
        self.assertLessEqual(max(real), 1)
        
        # negative test
        self.assertEqual((a-1,b), real.shape)
        
        
if __name__ == '__main__':
    unittest.main()
