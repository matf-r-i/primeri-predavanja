""" The :mod:`command_line` module is used for obtaining execution parameters for execution of the optimizers for max 
        ones problem.
"""

import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

import os
import logging
import datetime as dt
from collections import namedtuple
from argparse import ArgumentParser

DefaultCommandLineParameters = namedtuple('DefaultCommandLineParams', ['algorithm', 
                'optimization_type', 
                'outputFilePath', 
                'inputFilePath', 
                'inputFormat', 
                'maxNumberIterations', 
                'maxTimeForExecutionSeconds', 
                'randomSeed',
                'keepAllSolutionCodes',
                'kMin',
                'kMax',
                'maxLocalOptima',
                'localSearchType'
])

DEFAULT_COMMAND_LINE_PARAMETERS = DefaultCommandLineParameters('vns', 
                'maximization', 
                'outputs/max_ones_problem/dimension_25.txt', 
                'inputs/max_ones_problem/dimension_25.txt', 
                'txt', 
                100, 
                10, 
                0,
                False, 
                1,
                3,
                5,
                'local_search_best_improvement'
)

def parse_arguments():
        parser = ArgumentParser()

        subparsers = parser.add_subparsers(dest='algorithm')

        parser_vns = subparsers.add_parser('vns', help='Execute VNS metaheuristic for max_ones_problem.')
        parser_vns.add_argument('optimization_type', help='Decide if minimization or maximization will be executed.'
                , nargs='?', choices=('minimization', 'maximization'))
        parser_vns.add_argument('--outputFilePath', type=str, default='output/out.txt', 
                help=("File path of the output file. " 
                "File path '' means that it is within 'outputs' folder."))
        parser_vns.add_argument('--inputFilePath', type=str, default='inputs/max_ones_problem/dim_25.txt', 
                help='Input file path for the instance of the problem. ')
        parser_vns.add_argument('--inputFormat', type=str, choices=['txt', 'idle'], default = 'txt',
                help='Input file format. ')    
        parser_vns.add_argument('--maxNumberIterations', type=int, default=0, 
                help=("Maximum numbers of iterations during VNS execution. " 
                "Value 0 means that there is no limit on number of iterations.") )        
        parser_vns.add_argument('--maxTimeForExecutionSeconds', type=int, default=10, 
                help=("Maximum time for execution (in seconds).\n " 
                "Value 0 means that there is no limit on execution time.") )    
        parser_vns.add_argument('--randomSeed', type=int, default=0, 
                help=("Random seed for the VNS execution. " 
                "Value 0 means that random seed will be obtained from system timer.") )        
        parser_vns.add_argument('--keepAllSolutionCodes', type=bool, default=False, 
                help=("Should all solution codes be keep during metaheuristic execution.") )        
        parser_vns.add_argument('--kMin', type=int, default=1, 
                help=("VNS parameter k min.") )    
        parser_vns.add_argument('--kMax', type=int, default=3, 
                help=("VNS parameter k max.") )    
        parser_vns.add_argument('--maxLocalOptima', type=int, default=3, 
                help=("VNS parameter maximum number of local optima kept during execution.") )    
        parser_vns.add_argument('--localSearchType', type=str, 
                choices=['local_search_best_improvement', 'local_search_first_improvement'],  
                default='local_search_best_improvement', 
                help=("VNS parameter that determines local search type."))
        parser_vns.add_argument( "--log", default="warning", help=("Provide logging level. "
                "Example --log debug', default='warning'") )

        parser_idle = subparsers.add_parser('idle', help='Execute idle algorithm for max_ones_problem.')

        return parser.parse_args()

