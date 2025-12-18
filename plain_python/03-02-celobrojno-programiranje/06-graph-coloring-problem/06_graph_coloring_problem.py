import highspy
import linopy
import numpy as np
import pandas as pd
import networkx as nx

import matplotlib.pyplot as plt

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

verbosity:bool = True
path:str = 'plain_python/03-02-celobrojno-programiranje/06-graph-coloring-problem/data/drzave.txt'
graph = read_graph_file(path, verbosity)

nx.draw(graph)
plt.savefig( path[:len(path)-4] + '.png')

num_vertices = graph.number_of_nodes()
num_colors = num_vertices  # In the worst case, we might need as many colors as vertices

# Initialize Linopy model
model = linopy.Model()

# Add binary decision variables for each vertex and each color
vert_coord = pd.Index(range(num_vertices), name='vert_coord')
col_coord = pd.Index(range(num_colors), name='col_coord')
x_vars = model.add_variables(binary=True, coords=[vert_coord,col_coord], name='x')
y_vars = model.add_variables(binary=True, coords=[col_coord], name='y')

# Set objective function: minimize the number of colors used
model.add_objective( y_vars.sum(), sense='min')

# Add constraints: each vertex must be assigned exactly one color
for i in range(num_vertices):
    model.add_constraints((x_vars.loc[i, ]).sum() == 1)

# Add constraints: if a vertex is colored with a color, then that color must be used
for i in range(num_vertices):
    for k in range(num_colors):
        model.add_constraints(x_vars.loc[i, k] <= y_vars.loc[k])

# Add constraints: no two adjacent vertices can have the same color
for (ii, jj) in graph.edges:
    i:int = int(ii) - 1
    j:int = int(jj) -1
    for k in range(num_colors):
        model.add_constraints(x_vars.loc[i, k] + x_vars.loc[j, k] <= 1)

# Solve the model
model.solve(solver='highs')

print("{}:\n{}\n".format(x_vars, x_vars.solution))
print("{}:\n{}\n".format(y_vars, y_vars.solution))

# Output results
if model.status == 'ok':
    coloring = {}
    for i in range(num_vertices):
        for k in range(num_colors):
            if float(x_vars.solution.data[i, k]) > 0.5:
                coloring[i] = k
    print("Coloring of vertices:", coloring)
    print("Number of colors used:", sum(y_vars.solution.data[k] > 0.5 for k in range(num_colors)))
else:
    print("No optimal solution found.")    
