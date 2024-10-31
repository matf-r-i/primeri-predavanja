# This exercise describes
# • the TSP (Traveling Salesman Problem) problem, which has been first formulated in 1930 and is one of the most intensively studied problems in optimization,
# • its formulation, we will see formulation slightly more complex than the ones seen before 
# • solution by means of the ompr library, which is a higher-level (compared to lpSolveAPI) library to # interact with MILP solvers.
# 
# One definition for the TSP:
# The Traveling Salesman Problem (TSP) asks the following question: Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each
# city exactly once and returns to the origin city? 
# With this basic definition you have a set of vertices (cities) and a set of edges (connections between cities).
# Each edge has an associated distance d > 0. That distance could be travel time, distance in km or the monetary cost associated with traveling from one city to another. Restrictions on the distances lead to special cases of the problem.
# For example the metric-TSP requires that the triangle inequality holds for all triples of edges (as for the euclidean distance).
# In this exercise, we will construct a TSP with random points within an Euclidean space.

import math

import numpy as np
import pandas as pd
from plotnine import ggplot, aes, geom_line, geom_point, geom_segment

from itertools import combinations

import xarray as xr 
from linopy import Model

cities = ['A', 'B', 'C', 'D']
coordinates = {
    'A': (0, 0),
    'B': (1, 2),
    'C': (3, 1),
    'D': (4, 0)
}

# Calculate distances between cities
distances = {
    (i, j): np.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + 
                    (coordinates[i][1] - coordinates[j][1]) ** 2)
    for i, j in combinations(cities, 2)
}
print(distances)

# Create distance matrix
n = len(cities)
dist_matrix = np.zeros(shape=(n,n))
for i in range(n):
    dist_matrix[i,i] = 9999
    for j in range(i+1, n):
        c1 = cities[i]
        c2 = cities[j]
        d = distances[(c1,c2)] 
        dist_matrix[i,j] = d
        dist_matrix[j,i] = d
print(dist_matrix)

# Create the model
model = Model()

# Decision variables
x_coord = pd.Index(range(n), name='x_coord')
y_coord = pd.Index(range(n), name='y_coord')
x = model.add_variables(binary=True,  coords=[x_coord,y_coord], name='x')
print(x)
u = model.add_variables(integer=True, coords=[y_coord], name='u')
print(u)

# Objective function
model.add_objective( (x * dist_matrix).sum(), sense='min')

# Constraints
for i in range(n):
    model.add_constraints( (x.loc[i,]).sum() == 1)

for i in range(n):
    model.add_constraints( (x.loc[:,i]).sum() == 1)  

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model.add_constraints(u[i] - u[j] + n * x[i, j] <= n - 1)

for i in range(1, n):
    model.add_constraints(u[i] >= 1)
    model.add_constraints(u[i] <= n - 1)

print(model)   


model.solve()

print(model.solution)
