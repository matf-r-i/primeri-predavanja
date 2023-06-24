import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)

import os
import logging
import datetime as dt

from argparse import ArgumentParser


from collections import namedtuple


'''
Start command-line argument parsinig
'''
def parse_args_check_correctness():
    parser = ArgumentParser()
    subparser = parser.add_subparsers(dest='action')

    init_evaluate_write = subparser.add_parser('init_evaluate_write', 
        help="Initialize solution by RNG, evaluate it, and save it into specified file.")
    init_evaluate_write.add_argument('--solutionType', type=str, choices=[
        'simple',
        'complete'],
        required=True)
    init_evaluate_write.add_argument('--solutionNumberOfReels', type=int, 
        default=5)    
    init_evaluate_write.add_argument('--solutionReelMaxSize', type=int, 
        default=40)    
    init_evaluate_write.add_argument('--solutionNumberOfSymbols', type=int, 
        default=13)    
    init_evaluate_write.add_argument('--solutionTotalNumberOfElements', type=int, 
        default=160)    
    init_evaluate_write.add_argument('--solutionNumberOfRowsInWindow', type=int, 
        default=1)    
    init_evaluate_write.add_argument('--inputFilePath', type=str, 
        default='inputs/cleopatra-01.xlsx')
    #init_evaluate_write.add_argument('--inputFilePath', type=str, 
    #    default='inputs/small-one-01.xlsx')
    init_evaluate_write.add_argument('--evaluationType', type=str, choices=[
        'set1',
        'totalEnumeration',
        'monteCarlo',
        'theoretical',
        'partialEnumeration'],
        required=True)    
    init_evaluate_write.add_argument('--evaluationMonteCarloNumberOfRepetitions', type=int, 
        default=50000)    
    init_evaluate_write.add_argument('--outputFilePath', type=str, 
        default='outputs/cleopatra-01-99.xlsx')
    #init_evaluate_write.add_argument('--outputFilePath', type=str, 
    #    default='outputs/small-one-01-99.xlsx')
    init_evaluate_write.add_argument(
        "--log", 
        default="warning",
        help=(
            "Provide logging level. "
            "Example --log debug', default='warning'"),
    )

    read_evaluate_write = subparser.add_parser('read_evaluate_write', 
        help="Read solution from specified file, evaluate it, and save it into specified file.")
    read_evaluate_write.add_argument('--solutionType', type=str, choices=[
        'simple',
        'complete'],
        default='simple',
        required=True)
    read_evaluate_write.add_argument('--inputFilePath', type=str, 
        default='inputs/cleopatra-01.xlsx')
    #read_evaluate_write.add_argument('--inputFilePath', type=str, 
    #    default='inputs/small-one-01.xlsx')
    read_evaluate_write.add_argument('--evaluationType', type=str, choices=[
        'set1',
        'totalEnumeration',
        'monteCarlo',
        'theoretical',
        'partialEnumeration'],
        required=True)    
    read_evaluate_write.add_argument('--evaluationMonteCarloNumberOfRepetitions', type=int, 
        default=50000)    
    read_evaluate_write.add_argument('--outputFilePath', type=str, 
        default='outputs/cleopatra-01-99.xlsx')
    #read_evaluate_write.add_argument('--outputFilePath', type=str, 
    #    default='outputs/small-one-01-99.xlsx')
    read_evaluate_write.add_argument(
        "--log", 
        default="warning",
        help=(
            "Provide logging level. "
            "Example --log debug', default='warning'"),
    )

    return parser.parse_args()

def parse_args_symbol_order():
    parser = ArgumentParser()
    parser.add_argument('--inputFilePath', type=str, 
        default='inputs/cleopatra-01.xlsx')
    #parser.add_argument('--inputFilePath', type=str, 
    #   default='inputs/small-one-01.xlsx')
    parser.add_argument('--evaluationType', type=str, choices=[
        'totalEnumeration',
        'monteCarlo'],
        required=True)    
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


def parse_args_complete_case():
    parser = ArgumentParser()
    parser.add_argument('--inputFilePath', type=str, 
        default='inputs/cleopatra-01.xlsx')
    #parser.add_argument('--inputFilePath', type=str, 
    #   default='inputs/small-one-01.xlsx')
    parser.add_argument('--evaluationType', type=str, choices=[
        'totalEnumeration',
        'monteCarlo'],
        required=True)    
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

def parse_args_simple_case():
    parser = ArgumentParser()
    parser.add_argument('--inputFilePath', type=str, default='inputs/cleopatra-01.xlsx')
    #parser.add_argument('--inputFilePath', type=str, default='inputs/small-one-01.xlsx')
    parser.add_argument('--evaluationType', type=str, choices=[
        'totalEnumeration',
        'monteCarlo',
        'theoretical'],
        required=True)    
    parser.add_argument('--evaluationMonteCarloNumberOfRepetitions', type=int, 
        default=50000)    
    parser.add_argument('--maxNumberVnsIterations', type=int, 
        default=3000)    
    parser.add_argument('--maxTimeVnsExecutionSeconds', type=int, 
        default=0)    
    parser.add_argument('--outputFilePath', type=str, 
        default='outputs/cleopatra-01-99.xlsx')
    #parser.add_argument('--outputFilePath', type=str, 
    #   default='outputs/small-one-01-99.xlsx')
    parser.add_argument(
        "--log", 
        default="warning",
        help=(
            "Provide logging level. "
            "Example --log debug', default='warning'"),
    )
    return parser.parse_args()


'''
End command-line argument parsinig
'''
