import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent.parent.parent)

import unittest   

from algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer 

class Test_TestTargetProblem(unittest.TestCase):
    
    def setUp(self):
        self.__vns_optimizer = VnsOptimizer(evaluations_max=10)
        return
    
    def test_name_getter(self):
        self.assertEqual('vns', 'vns')

    def tearDown(self):
        return
    
if __name__ == '__main__':
    unittest.main()