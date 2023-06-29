import path

import sys

directory = path.Path(__file__).abspath()

sys.path.append(directory.parent)

sys.path.append(directory.parent.parent)

import optparse
import random

from datetime import datetime

from utils.files import ensure_dir 

from utils.logger import logger

from command_line import get_execution_parameters
from command_line import default_parameters


# Script should be executed from repository root folder
OPTIMIZATION_ALGORITHM_DIR = './optimization-algorithms/optimization_algorithms'
abs_path = path.Path(OPTIMIZATION_ALGORITHM_DIR).abspath()
sys.path.append(abs_path)
# Previous code should be commented out when pip install started to work


from target_problem.target_problem import TargetProblem

from algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from max_ones_problem_solving.max_ones_problem import MaxOnesProblem

from max_ones_problem_solving.max_ones_solution import MaxOnesSolution


def main():

    """ This function is an entry  point of the application.

    """

    OUTPUT_DIR = 'outputs'

    ensure_dir(OUTPUT_DIR)

    logger.debug('Execution started.')    

    problem = MaxOnesProblem('file_path')
    problem.load_from_file('clean')

    solution = MaxOnesSolution()

    optimizer = VnsOptimizer(is_minimization=False, evaluations_max=0, seconds_max=10, random_seed=0, 
            target_problem=problem, initial_solution=solution)
    logger.info('Optimizer: {}'.format(optimizer))

    logger.debug('Execution ended.')    



# This means that if this script is executed, then 

# main() will be executed

if __name__ == '__main__':
    main()


