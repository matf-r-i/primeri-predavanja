import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent)
sys.path.append(directory.parent.parent)

import optparse
import random

from datetime import datetime

from utils.logger import logger
from utils.logger import ensure_dir 

OUTPUT_DIR = 'outputs'

from utils.command_line import get_execution_parameters
from utils.command_line import default_parameters

# Script should be executed from repository root folder
OPTIMIZATION_ALGORITHM_DIR = './optimization-algorithms/optimization_algorithms'
abs_path = path.Path(OPTIMIZATION_ALGORITHM_DIR).abspath()
sys.path.append(abs_path)
# Previous code should be commented out when pip install started to work

from target_problem.target_problem import TargetProblem

from max_ones_problem_solving.max_ones_problem import MaxOnesProblem

def main():
    """ This function is an entry  point of the application.
    """
    ensure_dir(OUTPUT_DIR)
    logger.debug('Execution started.')    
    problem = MaxOnesProblem("aaa")
    logger.info('Problem: {}'.format(problem))
    logger.debug('Execution ended.')    


# This means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()

