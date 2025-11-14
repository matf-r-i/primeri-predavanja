import highspy
from linopy import Model

model = Model()

c = model.add_variables(lower=0, name="Number of chairs")
t = model.add_variables(lower=0, name="Number of tables")

model.add_constraints(5*c + 20*t <= 400, name="Mahogany constraint")
model.add_constraints(10*c + 15*t <= 450, name="Resources harnessing constraint")


model.add_objective(45*c + 80*t, sense='max')

print(model)

model.solve(solver='highs')

print("{}:{}\n".format(c, c.solution))
print("{}:{}\n".format(t, t.solution))

