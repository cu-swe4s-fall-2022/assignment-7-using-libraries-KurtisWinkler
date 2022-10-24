import unittest
import random
import numpy as np
import os
import sys
sys.path.append('/home/jovyan/assignment-7-using-libraries-KurtisWinkler')
import data_processor as dp  # nopep8

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.test_file_fixed = 'setup_test_file_fixed.txt'
        f_fixed = open(self.test_file_fixed, 'w')
        for i in range(100):
            f_fixed.write(str([i, i + 1, i + 2]) + '\n')
        f_fixed.close()
        
        self.test_file_rand = 'setup_test_file_rand.txt'
        f_rand = open(self.test_file_rand, 'w')
        self.rand_num = random.randint(1,100)
        for i in range(self.rand_num):
            rand_int = random.randint(1,100)
            f_rand.write(str([rand_int, rand_int * 2]) + '\n')
        f_rand.close()

        
    def tearDown(self):
        os.remove(self.test_file_fixed)
        os.remove(self.test_file_rand)
    
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
        
        # values >= 0real.min()
        self.assertGreaterEqual(real.min(), 0)
        
        # values <= 1
        self.assertLessEqual(real.max(), 1)
        
        # negative test
        self.assertNotEqual((1,1),real.shape)
                         
    def test_random_get_random_matrix(self):

        a = random.randint(1,10)
        b = random.randint(1,10)
        real = dp.get_random_matrix(a,b)
        
        # positve test
        self.assertEqual((a,b), real.shape)
        
        # values >= 0real.min()
        self.assertGreaterEqual(real.min(), 0)
        
        # values <= 1
        self.assertLessEqual(real.max(), 1)
        
        # negative test
        self.assertNotEqual((a-1,b), real.shape)
        
    # ***Test get_file_dimensions***
    def test_error_get_file_dimensions(self):

        # FileNotFoundError if input not integer
        self.assertRaises(FileNotFoundError, dp.get_file_dimensions, 'a.txt')

    def test_fixed_get_file_dimensions(self):

        real_dim = dp.get_file_dimensions(self.test_file_fixed)

        # positve test
        self.assertEqual((100, 3), real_dim)

        # negative test
        self.assertNotEqual((99, 3), real_dim)

    def test_rand_get_file_dimensions(self):

        real_dim = dp.get_file_dimensions(self.test_file_rand)

        # positve test
        self.assertEqual((self.rand_num, 2), real_dim)

        # negative test
        self.assertNotEqual((self.rand_num-1, 2), real_dim)



if __name__ == '__main__':
    unittest.main()
