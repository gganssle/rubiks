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
  utils.pprint(cube)
  print(plls[-1])
  print(f'{plls[-1][9:12]}  {plls[-1][18:21]}  {plls[-1][27:30]}')
  orientation = PLLSolver.PLLSolver(cube).get_orientations(cube)
  print(orientation)
  solution += PLLSolver.PLLSolver(cube).solution()
  times.append(time.time() - start)
  
print(plls)



