import highspy
from linopy import Model

m = Model()

a1 = m.add_variables(lower=0, name="placed in A at month 1")
a2 = m.add_variables(lower=0, name="placed in A at month 2")
a3 = m.add_variables(lower=0, name="placed in A at month 3")
a4 = m.add_variables(lower=0, name="placed in A at month 4")
a5 = m.add_variables(lower=0, name="placed in A at month 5")
a6 = m.add_variables(lower=0, name="placed in A at month 6")
b1 = m.add_variables(lower=0, name="placed in B at month 1")
b3 = m.add_variables(lower=0, name="placed in B at month 3")
b5 = m.add_variables(lower=0, name="placed in B at month 5")
c1 = m.add_variables(lower=0, name="placed in C at month 1")
c4 = m.add_variables(lower=0, name="placed in C at month 4")
d1 = m.add_variables(lower=0, name="placed in D at month 1")

m.add_objective(a1+b1+c1+d1, sense='min')

m.add_constraints(1.018*a1 - a2 <= 0, name="cash flow month 2 constraint le")
m.add_constraints(1.018*a1 - a2 >= 0, name="cash flow month 2 constraint ge")

m.add_constraints(1.035*b1 + 1.018*a2 - a3 - b3 <= 250, name="cash flow month 3 constraint le")
m.add_constraints(1.035*b1 + 1.018*a2 - a3 - b3 >= 250, name="cash flow month 3 constraint ge")

m.add_constraints(1.058* c1 + 1.018*a3 - a4 - c4 <= 0, name="cash flow month 4 constraint le")
m.add_constraints(1.058* c1 + 1.018*a3 - a4 - c4 >= 0, name="cash flow month 4 constraint ge")

m.add_constraints(1.035*b3 + 1.018*a4 - a5 - b5 <= 250, name="cash flow month 5 constraint le")
m.add_constraints(1.035*b3 + 1.018*a4 - a5 - b5 >= 250, name="cash flow month 5 constraint ge")

m.add_constraints(1.018*a5 - a6 <= 0, name="cash flow month 6 constraint le")
m.add_constraints(1.018*a5 - a6 >= 0, name="cash flow month 6 constraint ge")

m.add_constraints(1.11 * d1 + 1.058* c4 + 1.035*b5 + 1.018*a6 <= 300, name="cash flow month 7 constraint le")
m.add_constraints(1.11 * d1 + 1.058* c4 + 1.035*b5 + 1.018*a6 >= 300, name="cash flow month 7 constraint ge")


print(m)

m.solve(solver='highs')

print("{}:{}\n".format(a1, a1.solution))
print("{}:{}\n".format(a2, a2.solution))
print("{}:{}\n".format(a3, a3.solution))
print("{}:{}\n".format(a4, a4.solution))
print("{}:{}\n".format(a5, a5.solution))
print("{}:{}\n".format(a6, a6.solution))
print("{}:{}\n".format(b1, b1.solution))
print("{}:{}\n".format(b3, b3.solution))
print("{}:{}\n".format(b5, b5.solution))
print("{}:{}\n".format(c1, c1.solution))
print("{}:{}\n".format(c4, c4.solution))
print("{}:{}\n".format(d1, d1.solution))

