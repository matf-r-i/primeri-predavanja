
import math

import pandas as pd
from plotnine import ggplot, aes, geom_line, geom_point, geom_segment

import xarray as xr 
from linopy import Model

# Load data
cities = pd.read_csv('03-02-celobrojno-programiranje/05-traveling-salesperson-problem/data/cities_02.csv', usecols= ['x','y'])
print(cities)

# Draw loaded data on screen
draw = (
    ggplot(cities)  
    + aes(x="x", y="y")  
    + geom_point() 
)
print(draw)

def distance(i:int, j:int)->float:
    c1 = cities.loc[i]
    c2 = cities.loc[j]
    return math.sqrt( (c1.x-c2.x) * (c1.x-c2.x) 
            + (c1.y-c2.y) * (c1.y-c2.y))
#print(distance(1,2))

# Create distance matrix
n:int = cities.shape[0]
dists = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(distance(i,j))
    dists.append(row)
dist_matrix = xr.DataArray(dists, dims=['x_coord','y_coord']) 
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
