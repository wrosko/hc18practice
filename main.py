from manip import *
from filehandler import get_problem
from geneticalgorithm import *

problem = "small.in"
pizza, L, H = get_problem(problem)
print(pizza)

ga_loop(pizza, problem[:-3], (L,H), n_generations=10000, population_size=25, n_elite=5, crossover_prob=0.4, mutation_prob=1)