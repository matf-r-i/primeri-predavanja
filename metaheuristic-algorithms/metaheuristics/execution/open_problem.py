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

from problems.max_ones.target_problem_max_ones import TargetProblemMaxOnes

def main():
    """ This function is an entry  point of the application.
    """
    problem = TargetProblemMaxOnes("aaa")
    print(problem)


# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()

