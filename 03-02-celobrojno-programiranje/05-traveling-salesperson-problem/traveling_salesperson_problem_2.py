
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
#print(draw)

def distance(i:int, j:int)->float:
    c1 = cities.loc[i]
    c2 = cities.loc[j]
    return math.sqrt( (c1.x-c2.x) * (c1.x-c2.x) 
            + (c1.y-c2.y) * (c1.y-c2.y))
#print(distance(1,2))

# Create distance matrix
LARGE:float = 99999999
n:int = cities.shape[0]
dists = []
for i in range(n):
    row = []
    for j in range(n):
        if i != j:
            row.append(distance(i,j))
        else:
            row.append(LARGE)
    dists.append(row)
dist_matrix = xr.DataArray(dists, dims=['x_coord','y_coord']) 
print(dist_matrix)

# Create the model
model = Model()

# Decision variables
x_coord = pd.Index(range(n), name='x_coord')
y_coord = pd.Index(range(n), name='y_coord')
u_coord = pd.Index(range(n), name='u_coord')
x = model.add_variables(binary=True,  coords=[x_coord,y_coord], name='x')
print(x)
u = model.add_variables(integer=True, coords=[u_coord], name='u')
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

start = []
for i in range(n):
    if u.solution.data[i] == 0:
        start.append([cities.loc[i].x, cities.loc[i].y])
start = pd.DataFrame(start, columns=['x', 'y'])
#print(selected)

links = []
for i in range(n):
    for j in range(i+1, n):
        if u.solution.data[i] >= 0 and u.solution.data[j]>=0 and \
            (abs(u.solution.data[i]-u.solution.data[j]) in (1,n-1) ):
            x1 = cities.loc[u.solution.data[i]].x
            y1 = cities.loc[u.solution.data[i]].y
            x2 = cities.loc[u.solution.data[j]].x
            y2 = cities.loc[u.solution.data[j]].y
            links.append([x1,y1,x2,y2])
links = pd.DataFrame(links, columns=['x1', 'y1', 'x2', 'y2'])
#print(links)

# Draw results data on screen
draw = (
    ggplot(cities)  
    + aes(x="x", y="y")  
    + geom_point() 
    + geom_point(data = start,color = "yellow")
)
for i in range(len(links)):
    draw += geom_segment(mapping = aes(x=links.loc[i].x1, y=links.loc[i].y1, 
            xend=links.loc[i].x2, yend=links.loc[i].y2), color="pink")
print(draw)