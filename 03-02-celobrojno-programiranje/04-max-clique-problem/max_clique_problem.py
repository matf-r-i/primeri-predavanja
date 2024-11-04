from datetime import datetime
import sys
from math import floor
from linopy import Model
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def read_graph_file(file_path:str, verbosity: bool)->nx.Graph:

    edges = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('c'):  # graph description
                if verbosity:
                    print(*line.split()[1:])
            # first line: p name num_of_vertices num_of_edges
            elif line.startswith('p'):
                _, name, vertices_num, edges_num = line.split()
                if verbosity:
                    print('{0} {1} {2}'.format(name, vertices_num, edges_num))
            elif line.startswith('e'):
                _, v1, v2 = line.split()
                edges.append((v1, v2))
            else:
                continue
        return nx.Graph(edges)

def get_max_clique_problem(graph: nx.Graph)->Model:

    model = Model()

    x_coord = pd.Index(range(len(graph.nodes)), name='x_coord')
    x = model.add_variables(binary=True, coords=[x_coord], name='x')    
    
    # Add objective function
    model.add_objective(x.sum(), sense = 'max')
    
    # Add constraints to ensure no two selected vertices are adjacent
    for i in range(len(graph.nodes)):
        for j in range(i+1, len(graph.nodes)):
            if not graph.has_edge(str(i+1), str(j+1)):
                model.add_constraints(x.loc[i] + x.loc[j] <= 1)
    return model


verbosity:bool = True
path:str = '03-02-celobrojno-programiranje/04-max-clique-problem/data/graph_01.txt'
graph = read_graph_file(path, verbosity)

nx.draw(graph)
plt.savefig( path[:len(path)-4] + '.png')

problem_max_clique = get_max_clique_problem(graph)
problem_max_clique.solve()


print(problem_max_clique.solution)


