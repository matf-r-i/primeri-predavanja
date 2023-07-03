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
            # set optimization type (minimization or maximization)
            if parameters.optimization_type == 'minimization':
                is_minimization:bool = True
            elif parameters.optimization_type == 'maximization':
                is_minimization = False
            else:
                raise ValueError("Either minimization or maximization should be selected.")
            # output file path setup
            if parameters.outputFilePath is not None and  parameters.outputFilePath != '':
                output_file_path_parts:list[str] = parameters.outputFilePath.split('/')
            else:
                output_file_path_parts:list[str] = ['outputs', 'out']
            output_file_name_ext:str = output_file_path_parts[-1]
            output_file_name_parts:list[str] = output_file_name_ext.split('.')
            if len(output_file_name_parts) > 1:
                output_file_ext:str = output_file_name_parts[-1]
                output_file_name_parts.pop()
                output_file_name = '.'.join(output_file_name_parts)
            else:
                output_file_ext = 'txt'
                output_file_name = output_file_name_parts[0]
            dt = datetime.now()
            output_file_path_parts.pop()
            output_file_dir:str =  '/'.join(output_file_path_parts)
            output_file_path_parts.append( output_file_name +  '-' + parameters.algorithm + '-' +
                    parameters.optimization_type[0:3] + '-' + dt.strftime("%Y-%m-%d-%H-%M-%S.%f") + '.' + 
                    output_file_ext)
            output_file_path:str = '/'.join(output_file_path_parts)
            logger.debug("Output file path: {}".format(output_file_path))
            # open and write to output file
            ensure_dir(output_file_dir)
            output_file = open(output_file_path, "w", encoding="utf-8")
            start_time = datetime.now()
            output_file.write("VNS started at: %s\n" % str(start_time))
            output_file.write('Execution parameters: {}\n'.format(parameters))
            # set random seed
            if( int(parameters.randomSeed) > 0 ):
                r_seed:int = int(parameters.randomSeed)
                logger.info("RandomSeed is predefined. Predefined seed value:  %d" % r_seed)
                output_file.write("RandomSeed is predefined. Predefined seed value:  %d\n" % r_seed)
                random.seed(r_seed)
            else:
                r_seed = random.randrange(sys.maxsize)
                logger.info("RandomSeed is not predefined. Generated seed value:  %d" % r_seed)
                output_file.write("RandomSeed is not predefined. Generated seed value:  %d\n" % r_seed)
                random.seed(r_seed)
            # problem to be solved
            problem = MaxOnesProblem(parameters.inputFilePath)
            problem.load_from_file(parameters.inputFormat)
            logger.debug( 'Problem: {}'.format(problem))
            # initial solution for solving
            initial_solution = MaxOnesSolution(problem=problem)
            initial_solution.random_init()
            logger.debug('Initial solution: {}'.format(initial_solution))
            # optimizer used for solving problem 
            optimizer = VnsOptimizer(is_minimization=is_minimization, evaluations_max=parameters.maxNumberIterations, 
                    seconds_max=parameters.maxTimeForExecutionSeconds, random_seed=r_seed, 
                    keep_all_solution_codes=False, target_problem=problem, initial_solution=initial_solution)
            logger.debug('Optimizer: {}'.format(optimizer))
            optimizer.optimize()
            logger.info('Best solution: {}'.format(optimizer.best_solution))            
            logger.debug('VNS ended.')
        elif parameters.algorithm == 'idle':
            logger.debug('Idle execution started.')    
            logger.debug('Idle execution ended.')    
        else:
            raise ValueError("Invalid optimization algorithm is chosen.")
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


