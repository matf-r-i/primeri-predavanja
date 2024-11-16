from linopy import Model

m = Model()

c = m.add_variables(lower=0, name="Number of chairs")
t = m.add_variables(lower=0, name="Number of tables")

m.add_constraints(5*c + 20*t <= 400, name="Mahogany constraint")
m.add_constraints(10*c + 15*t <= 450, name="Resources harnessing constraint")


m.add_objective(45*c + 80*t, sense='max')

print(m)

m.solve()

print("{}:{}\n".format(c, c.solution))
print("{}:{}\n".format(t, t.solution))

