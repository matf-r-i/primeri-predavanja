"""
This script reads and solves a linear programming problem defined in an LP file using the HiSpy library.

It performs the following steps:
1. Initializes the HiSpy solver object.
2. Reads the model from the specified `.lp` file.
3. Runs the solver to find the optimal solution.
4. Retrieves and prints various status and solution information from the solver object.

Assumes the existence of a file named 'electro-poly.lp' in the same directory.
"""
import highspy
h = highspy.Highs()

file_name = 'electro-poly.lp'
# Reads the model definition from the specified LP file.
status = h.readModel(file_name)
print('Reading model file ', file_name, ' returns a status of ', status)

# Runs the optimization algorithm on the loaded model.
h.run()

# Retrieves the solution, basis, and general information from the solver.
solution = h.getSolution()
basis = h.getBasis()
info = h.getInfo()
model_status = h.getModelStatus()

# Prints various diagnostic and solution metrics.
print('Model status = ', h.modelStatusToString(model_status))
print()
print('Optimal objective = ', info.objective_function_value)
print('Iteration count = ', info.simplex_iteration_count)
print('Primal solution status = ', h.solutionStatusToString(info.primal_solution_status))
print('Dual solution status = ', h.solutionStatusToString(info.dual_solution_status))
print('Basis validity = ', h.basisValidityToString(info.basis_validity))
print('Solution values:', solution.col_value)