from rubik_solver import utils, Cubie
from rubik_solver.Solver.CFOP import F2LSolver, OLLSolver, PLLSolver
from rubik_solver.Solver.Beginner import WhiteCrossSolver
from rubik_solver.Move import Move
import copy, time

cube = Cubie.Cube()
cube.shuffle()

times = []
plls = []

for i in range(3):
  cube.shuffle()
  # print(cube.to_naive_cube().get_cube())

  # start = time.time()
  # utils.solve(cube, 'CFOP')
  # print(f'solve time: {time.time() - start}')

  start = time.time()
  cube = copy.deepcopy(cube)
  solution = WhiteCrossSolver.WhiteCrossSolver(cube).solution()
  solution += F2LSolver.F2LSolver(cube).solution()
  solution += OLLSolver.OLLSolver(cube).solution()
  plls.append(cube.to_naive_cube().get_cube())
  solution += PLLSolver.PLLSolver(cube).solution()
  # utils.pprint(cube)
  times.append(time.time() - start)
  
print(plls)



