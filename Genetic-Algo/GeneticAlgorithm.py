import random
import numpy as np
import matplotlib.pyplot as plt
from geneticalgorithm import geneticalgorithm as ga

capacityBeforeOptimization = []
capacityAfterOptimization = []

choice=0
try:
    choice = int(input("Which problem statement file do you want to choose: \n"
                   " 1) input.txt \n"
                   " 2) testing.txt  \n"))
except :
    print("Please enter 1 or 2 only in numbers.")
else:
    if choice == 1:
        fileName = "input.txt"
    elif choice == 2:
        fileName = "testing.txt"

    with open(fileName, 'r') as file:
        fileContents = file.read().split("\n")

    numberOfUnits = fileContents[0]  # POPULATION_SIZE
    numberOfIntervals = fileContents[1]  # LEN_CHROMOSOME
    split = 2


def load_chromosomes():
    chromosome=[]
    for index in range(2,len(fileContents)):
        line_splited= fileContents[index].split(",")
        x = [0,0,0,0]
        capacityBeforeOptimization.append(int(line_splited[1]))
        for i in range(int(line_splited[2])):
            x[random.randint(0,3)] = 1
        #chromosome.append(x,int(line_splited[1]))
        chromosome.append(x)
    return chromosome

def create_chromosome():
    chromosome = []
    for i in range(numberOfIntervals):
        if random.random() > 0.5:
            chromosome.append(1)
        else:
            chromosome.append(0)
    return chromosome


def create_population():
    population = []
    for i in range(numberOfUnits):
        a = create_chromosome()
        population.append(a)
    return population


def cost(chromosome_tuple):
    return chromosome_tuple[1]


def fitness(chromosome):
      return sum(chromosome)*20


def population_with_fitness(population):
    pop_fit = []
    for i in population:
        a = (i, fitness(i))
        pop_fit.append(a)

    return sorted(pop_fit, key=cost, reverse=True)


def selection(population):
    return population[:4]


def crossover(selection):
    cross_list = []
    for i in range(0, len(selection), 2):
        p1 = selection[i][0]
        p2 = selection[i + 1][0]

        c1 = p1[:split] + p2[split:]
        c2 = p2[:split] + p1[split:]

        cross_list.append(p1)
        cross_list.append(p2)
        cross_list.append(c1)
        cross_list.append(c2)
    return cross_list


def mutation(crs):
    mut = []
    for a in crs:
        ind = random.randint(0, len(a) - 1)
        if a[ind] == 1:
            a[ind] = 0
        else:
            a[ind] = 1
        mut.append(a)
    return mut


def show(population, generation):
    #population = selection(pop)
    print('Generation no [', generation, ']', 'Best Chromosome: ', population[0][0], 'Fitness: ', population[0][1])
    print(80 * '-')
    for no, i in enumerate(population):
        print('chromosome # ', no + 1, '<<<', i[0], '>>>', 'Fitness:', i[1])



def run():
    Population = None
    for i in range(100):
        if Population is None:
            Population = load_chromosomes()
            Population1 = population_with_fitness(Population)
        else:
            show(Population1, i)
            Population1 = selection(Population1)
            Population1 = crossover(Population1)
            print(Population1)
            Population1 = mutation(Population1)
            print("c",Population1)
            Population1 = population_with_fitness(Population1)

            # if (Population1[0][1] == 80):
            #     show(Population1, i)
            #     break

    for i in Population1:
        capacityAfterOptimization.append(i[1])

if __name__ == "__main__":
   # print(load_chromosomes())
    run()
    print(capacityBeforeOptimization, capacityAfterOptimization)
    plt.plot(capacityBeforeOptimization, color='r', marker= 'o')
    plt.plot(capacityAfterOptimization, color='g', marker='o')
    plt.xlabel("No of Intervals")
    plt.ylabel("Capacity (MW)")
    plt.title("Optimization using genetic algorithm")
    plt.legend(['Before Optimization','Optimized'])
    plt.savefig("Optimization_using_genetic_algorithm.png")
    plt.grid()
    plt.show()

