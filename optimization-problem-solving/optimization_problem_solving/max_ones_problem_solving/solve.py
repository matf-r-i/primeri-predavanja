import path

import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

import random
from datetime import datetime
from collections import namedtuple

# Script should be executed from repository root folder
OPTIMIZATION_ALGORITHM_DIR = './optimization-algorithms/optimization_algorithms'
abs_path = path.Path(OPTIMIZATION_ALGORITHM_DIR).abspath()
sys.path.append(abs_path)
# Previous code should be commented out when pip install started to work

from utils.files import ensure_dir 

from utils.logger import logger

from command_line import parse_arguments

from algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from max_ones_problem_solving.max_ones_problem import MaxOnesProblem

from max_ones_problem_solving.max_ones_solution import MaxOnesSolution

def main():
    """ 
    This function executes VNS.
    """
    logger.debug('Solver started.')    
    try:
        parameters = parse_arguments()        

        logger.info('Execution parameters: {}'.format(parameters))

        if parameters.algorithm == 'vns':
            logger.debug('VNS started.') 
            problem = MaxOnesProblem(parameters.inputFilePath)
            problem.load_from_file(parameters.inputFormat)
            solution = MaxOnesSolution()
            optimizer = VnsOptimizer(is_minimization=False, evaluations_max=0, seconds_max=10, random_seed=0, 
                    keep_all_solution_codes=False, target_problem=problem, initial_solution=solution)
            logger.info('Optimizer: {}'.format(optimizer))
            logger.debug('VNS ended.')
        elif parameters.algorithm == 'idle':
            logger.debug('Idle execution started.')    
            logger.debug('Idle execution ended.')    
        else:
            raise ValueError("Invalid algorithm")
        logger.debug('Solver ended.')    
        return
    except Exception as exp:
        if hasattr(exp, 'message'):
            logger.exception('Exception: %s\n' % exp.message)
        else:
            logger.exception('Exception: %s\n' % str(exp))
        

# This means that if this script is executed, then 
# main() will be executed

if __name__ == '__main__':
    main()


