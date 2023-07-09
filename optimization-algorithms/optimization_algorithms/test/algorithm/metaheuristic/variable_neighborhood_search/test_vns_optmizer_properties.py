import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent.parent.parent.parent)

import unittest   

from algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer 

class TestVnSOptimizerProperties(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass\n")

    def setUp(self):
        self.__evaluations_max = 42
        self.__vns_optimizer = VnsOptimizer(evaluations_max=self.__evaluations_max, seconds_max=42, random_seed=42, 
                keep_all_solution_codes=True, target_problem=None, initial_solution=None, k_min=3, k_max=42, 
                max_local_optima=42, local_search_type='first_improvement')
        return
    
    def test_name_should_be_vns(self):
        self.assertEqual(self.__vns_optimizer.name, 'vns')

    def test_evaluation_max_should_be_equal_as_in_constructor(self):
        self.assertEqual(self.__vns_optimizer.evaluations_max, self.__evaluations_max)

    def tearDown(self):
        return

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass")
    
if __name__ == '__main__':
    unittest.main()