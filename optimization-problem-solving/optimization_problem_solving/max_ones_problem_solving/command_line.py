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

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument(
            "--log", 
            default="warning",
            help=(
                "Provide logging level. "
                "Example --log debug', default='warning'"),
        )

    subparsers = parser.add_subparsers(dest='algorithm')
    
    parser_vns = subparsers.add_parser('vns', help='VNS for max_ones_problem help')
    parser_vns.add_argument('--inputFilePath', type=str, 
        default='inputs/max_ones_problem/dim_25.txt')
    parser_vns.add_argument('--inputFormat', type=str, choices=[
        'txt',
        'idle'], default = 'txt')    
    parser_vns.add_argument('--outputDirectory', type=str, 
        default='outputs/max_ones_problem')
    parser_vns.add_argument('--maxTimeForExecutionSeconds', type=int, 
        default=10)    
    parser_vns.add_argument('--maxNumberIterations', type=int, 
        default=0)    

    parser_idle = subparsers.add_parser('idle', help='Idle algorithm help')

    return parser.parse_args()

