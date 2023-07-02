import path

import sys

directory = path.Path(__file__).abspath()

sys.path.append(directory.parent)

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

from command_line import get_execution_parameters
from command_line import default_parameters

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
    # reading command-line arguments and options
    parser = optparse.OptionParser()
    parser.set_defaults(debug=False,xls=False)
    parser.add_option('--debug', action='store_true', dest='debug')
    parser.add_option('--verbose', action='store_true', dest='verbose')
    (options, args) = parser.parse_args()
    try:
        # Obtaining execution parameters
        parameters = get_execution_parameters(options, args, default_parameters)
        logger.info('Execution parameters: {}'.format(parameters))
        algorithm = parameters['Algorithm']
        input_file_path = parameters['InputFilePath']
        input_format = parameters['InputFormat']
        
        if algorithm == 'vns':
            logger.debug('vns execution started')
            problem = MaxOnesProblem(input_file_path)
            problem.load_from_file(input_format)
            solution = MaxOnesSolution()
            optimizer = VnsOptimizer(is_minimization=False, evaluations_max=0, seconds_max=10, random_seed=0, 
                    keep_all_solution_codes=False, target_problem=problem, initial_solution=solution)
            logger.info('Optimizer: {}'.format(optimizer))
        elif algorithm == 'idle':
            logger.debug('No execution is required')
        else:
            logger.info("Incorrect algorithm '" + algorithm + "', should be one of: vns, idle \n") 
            return
        logger.debug('Execution ended.')    
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


