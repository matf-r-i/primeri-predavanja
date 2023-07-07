import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

import unittest   

from optimization_algorithms.target_problem.target_problem import TargetProblem  

class Test_TestTargetProblem(unittest.TestCase):
    
    def setUp(self):
        self.__target_problem = TargetProblem(name='Miki', file_path='Paja', is_minimization = True)
    
    def test_name_getter(self):
        self.assertEqual(self.__target_problem.name, 'Miki')

    def test_file_path_getter(self):
        self.assertEqual(self.__target_problem.file_path, 'Paja')

    def test_is_minimization_getter(self):
        self.assertTrue(self.__target_problem.is_minimization)

    def tearDown(self):
        pass
    
if __name__ == '__main__':
    unittest.main()