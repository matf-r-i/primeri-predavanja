import highspy
import math
import xarray as xr 
from linopy import Model

m = Model()

lower = xr.DataArray([0,0,0,0], dims=['from'])
upper = xr.DataArray([math.inf], dims=['to'])

x = m.add_variables(lower=lower, upper=upper, name='x')

print(x)


# Overall production
m.add_constraints(x.loc[0,0] + x.loc[1,0] + x.loc[2,0] + x.loc[3,0] == 8)

# mix consists of at least 20% corn  
m.add_constraints((0.3*x.loc[0,0] + 0.05*x.loc[1,0] + 0.2*x.loc[2,0] + 0.1*x.loc[3,0])/8 >= 0.2)


# mix consists of at least 15% grain  
m.add_constraints((0.1*x.loc[0,0] + 0.3*x.loc[1,0] + 0.15*x.loc[2,0] + 0.1*x.loc[3,0])/8 >= 0.15)

# mix consists of at least 15% minerals  
m.add_constraints((0.2*x.loc[0,0] + 0.2*x.loc[1,0] + 0.2*x.loc[2,0] + 0.3*x.loc[3,0])/8 >= 0.15)

m.add_objective( 250*x.loc[0,0] + 300*x.loc[1,0] + 320*x.loc[2,0] + 150*x.loc[3,0])

print(m)

m.solve(solver='highs')

print(m.solution)


print("{}:\n{}\n".format(x, x.solution))

