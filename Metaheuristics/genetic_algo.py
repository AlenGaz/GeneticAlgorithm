import time
from functools import partial
from problems import knapsack
from algorithms import bruteforce, genetic
from utils.analyze import timer

things = knapsack.generate_things(22)
things = knapsack.second_example

weight_limit = 12600

print("Weight Limit: %d g" % weight_limit)
print("")
print("BRUTEFORCE")
print("----------")

#with timer():
bruteStartT= time.time()
result = bruteforce(things, weight_limit)
bruteEndT = time.time()
bruteTime = (bruteEndT - bruteStartT)
print("elapsed time: " + str(bruteTime))
knapsack.print_stats(result[1])

print("")
print("GENETIC ALGORITHM")
print("----------")

geneticStartT = time.time()
population, generations = genetic.run_evolution(
	populate_func=partial(genetic.generate_population, size=20, genome_length=len(things)),
	fitness_func=partial(knapsack.fitness, things=things, weight_limit=weight_limit),
	fitness_limit=result[0],
	generation_limit=100
)
geneticEndT= time.time()
geneticTime = (geneticEndT - geneticStartT)
print("elapsed time: " + str(geneticTime))

sack = knapsack.from_genome(population[0], things)
knapsack.print_stats(sack)


print("------------")
print("Bruteforce/Genetic time:  " + str((bruteTime/geneticTime)))


