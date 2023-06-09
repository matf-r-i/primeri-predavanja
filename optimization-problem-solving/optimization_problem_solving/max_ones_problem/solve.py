import path
import sys

# Script should be executed from repository root folder
OPTIMIZATION_ALGORITHM_DIR = './optimization-algorithms/optimization_algorithms'
abs_path = path.Path(OPTIMIZATION_ALGORITHM_DIR).abspath()
sys.path.append(abs_path)
# Previous code should be commented out when pip install started to work


directory = path.Path(__file__).abspath()
sys.path.append(directory.parent)

from random import randrange
from random import seed
from datetime import datetime
from collections import namedtuple

from algorithm.metaheuristic.variable_neighborhood_search.vns_optimizer import VnsOptimizer

from utils.files import ensure_dir 
from utils.logger import logger
from command_line import default_parameters_cl
from command_line import parse_arguments
from max_ones_problem import MaxOnesProblem
from max_ones_problem_binary_representation_solution import MaxOnesProblemBinaryRepresentationSolution

def main():
    """ 
    This function executes VNS.
    """
    logger.debug('Solver started.')    
    try:
        parameters = default_parameters_cl
        read_parameters_cl = parse_arguments()
        for param_key_value in read_parameters_cl._get_kwargs():
            key:str = param_key_value[0]
            val = param_key_value[1]
            logger.debug('key:{} value:{}'.format(key, val))
            if key is not None and val is not None:
                parameters[key] = val
        logger.debug('Execution parameters: {}'.format(parameters))
        if parameters['algorithm'] == 'vns':
            logger.debug('VNS started.') 
            # set optimization type (minimization or maximization)
            if parameters['optimization_type'] == 'minimization':
                is_minimization:bool = True
            elif parameters['optimization_type'] == 'maximization':
                is_minimization:bool = False
            else:
                raise ValueError("Either minimization or maximization should be selected.")
            # output setup
            if parameters['writeToOutputFile'] is None:
                write_to_output_file:bool = False
            else:
                write_to_output_file:bool = bool(parameters['writeToOutputFile'])
            if parameters['outputFilePath'] is not None and  parameters['outputFilePath'] != '':
                output_file_path_parts:list[str] = parameters['outputFilePath'].split('/')
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
            output_file_path_parts.append( output_file_name +  '-' + parameters['algorithm'] + '-' +
                    parameters['optimization_type'][0:3] + '-' + dt.strftime("%Y-%m-%d-%H-%M-%S.%f") + '.' + 
                    output_file_ext)
            output_file_path:str = '/'.join(output_file_path_parts)
            logger.debug("Output file path: {}".format(output_file_path))
            ensure_dir(output_file_dir)
            output_file = open(output_file_path, "w", encoding="utf-8")
            start_time = datetime.now()
            if write_to_output_file:
                output_file.write("# VNS started at: %s\n" % str(start_time))
                output_file.write('# Execution parameters: {}\n'.format(parameters))
            # input file setup
            input_file_path:str = parameters['inputFilePath']
            input_format:str = parameters['inputFormat']
            # finishing criteria setup
            max_number_iterations:int = parameters['maxNumberIterations']
            max_time_for_execution_in_seconds = parameters['maxTimeForExecutionSeconds']
            # random seed setup
            if( int(parameters['randomSeed']) > 0 ):
                r_seed:int = int(parameters['randomSeed'])
                logger.info("RandomSeed is predefined. Predefined seed value:  %d" % r_seed)
                if write_to_output_file:
                    output_file.write("# RandomSeed is predefined. Predefined seed value:  %d\n" % r_seed)
                random.seed(r_seed)
            else:
                r_seed = randrange(sys.maxsize)
                logger.info("RandomSeed is not predefined. Generated seed value:  %d" % r_seed)
                if write_to_output_file:
                    output_file.write("# RandomSeed is not predefined. Generated seed value:  %d\n" % r_seed)
                seed(r_seed)
            # evaluation cache setup
            evaluation_cache_is_used:bool = parameters['evaluationCacheIsUsed']
            # calculation distances cache setup
            calculation_solution_distance_cache_is_used = parameters['calculationSolutionDistanceCacheIsUsed']
            # bookkeeping setup
            keep_all_solution_codes:bool = parameters['keepAllSolutionCodes']
            # parameters for VNS process setup
            k_min:int = parameters['kMin']
            k_max:int = parameters['kMax']
            max_local_optima = parameters['maxLocalOptima']
            local_search_type = parameters['localSearchType']
            # problem to be solved
            problem = MaxOnesProblem(input_file_path)
            problem.load_from_file(input_format)
            # initial solution for solving
            initial_solution = MaxOnesProblemBinaryRepresentationSolution()
            initial_solution.evaluation_cache_cs.is_caching = evaluation_cache_is_used
            initial_solution.random_init(problem=problem)
            #logger.debug('Initial solution: {}'.format(initial_solution))
            # optimizer used for solving
            optimizer = VnsOptimizer(evaluations_max=max_number_iterations, 
                    seconds_max=max_time_for_execution_in_seconds, random_seed=r_seed, 
                    keep_all_solution_codes=keep_all_solution_codes, target_problem=problem, 
                    initial_solution=initial_solution, k_min=k_min, k_max=k_max, max_local_optima=max_local_optima, 
                    local_search_type=local_search_type)
            #logger.debug('Optimizer: {}'.format(optimizer))
            optimizer.optimize()
            optimizer.solution_code_distance_cache_cs.is_caching = calculation_solution_distance_cache_is_used
            optimizer.output_control.write_to_output_file = write_to_output_file
            optimizer.output_control.output_file = output_file
            logger.info('Best solution: {}'.format(optimizer.best_solution))            
            logger.debug('Optimizer: {}'.format(optimizer))
            logger.debug('VNS ended.')
        elif parameters['algorithm'] == 'idle':
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


