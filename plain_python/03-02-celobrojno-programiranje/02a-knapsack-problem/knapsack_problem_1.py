import highspy
import xarray as xr
from linopy import Model

m = Model()

x1 = m.add_variables(binary=True, name='x1')
x2 = m.add_variables(binary=True, name='x2')
x3 = m.add_variables(binary=True, name='x3')
x4 = m.add_variables(binary=True, name='x4')
x5 = m.add_variables(binary=True, name='x5')
x6 = m.add_variables(binary=True, name='x6')

print(m.variables)

# constraints
m.add_constraints(5*x1+7*x2+4*x3+3*x4+4*x5+6*x6 <= 14, name="total points constraint")

# objective
m.add_objective(16*x1+22*x2+12*x3+8*x4+11*x5+19*x6, sense='max')

print(m)

m.solve(solver='highs')

print(m.solution)

print(x1.solution)
print(x2.solution)
print(x3.solution)
print(x4.solution)
print(x5.solution)
print(x6.solution)
