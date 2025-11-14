from linopy import Model

model = Model()

m = model.add_variables(lower=0, name="Opportunity cost of mahogany")
l = model.add_variables(lower=0, name="Opportunity cost of labor")

model.add_constraints(5*m + 10*l >= 45, name="Chairs constraint")
model.add_constraints(20*m + 15*l >= 80, name="Tables constraint")


model.add_objective(400*m + 450*l, sense='min')

print(model)

model.solve()

print("{}:{}\n".format(m, m.solution))
print("{}:{}\n".format(l, l.solution))

