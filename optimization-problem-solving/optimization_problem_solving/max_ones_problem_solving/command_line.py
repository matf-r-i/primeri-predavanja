""" The :mod:`command_line` module is used for obtaining execution parameters for execution of the 
    optimizers for max ones problem.

"""

import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

import os
import logging
import datetime as dt

from argparse import ArgumentParser

from collections import namedtuple


def parse_args_complete_case():
    parser = ArgumentParser()
    parser.add_argument('--algorithm', type=str, choices=[
        'vns',
        'idle'],
        required=True)    
    parser.add_argument('--inputFilePath', type=str, 
        default='inputs/max_ones_problem/dim_25.txt')
    parser.add_argument('--evaluationMonteCarloNumberOfRepetitions', type=int, 
        default=50000)    
    parser.add_argument('--maxNumberVnsIterations', type=int, 
        default=3000)    
    parser.add_argument('--maxTimeVnsExecutionSeconds', type=int, 
        default=0)    
    parser.add_argument('--outputFilePath', type=str, 
        default='outputs/cleopatra-01-99.xlsx')
    #parser.add_argument('--outputFilePath', type=str, default='outputs/small-one-01-99.xlsx')
    parser.add_argument(
        "--log", 
        default="warning",
        help=(
            "Provide logging level. "
            "Example --log debug', default='warning'"),
    )
    return parser.parse_args()

