import random
import numpy as np

def f(x):
    return - (x ** 2 / 10) + 3 * x 

         
def generate_population(population_size):
    population = []
    for i in range(population_size):
        x = random.randint(0, 31)
        population.append(x)
    print(f'Population of x:{population}')    
    return population

def selection_probability(fitness_values):  #g(x)
  select_probability = []
  summation = sum(fitness_values)
  for i in range(0,len(fitness_values)):
    select_probability.append(fitness_values[i]/summation)
  return select_probability

def calculate_fitness(population):
    fitness_values = []
    for x in population:
        fitness_values.append(f(x))
    #print(f'fitness values f(x): {fitness_values}')    
    return fitness_values

def crossover(chromosome1, chromosome2):
    crossover_point = random.randint(0, len(chromosome1)-1)
    new_chromosome1 = chromosome1[:crossover_point] + chromosome2[crossover_point:]
    new_chromosome2 = chromosome2[:crossover_point] + chromosome1[crossover_point:]
    return new_chromosome1, new_chromosome2

'''def mutation(chromosome):
    mutation_point = random.randint(0,len(chromosome)-1)
    if chromosome[mutation_point] == 0:
        chromosome[mutation_point] = 1
    else:
        chromosome[mutation_point] = 0
    return chromosome '''   

def get_next_generation(population, fitnesses):
    next_population = []
    while len(next_population) < len(population):
        parent1 = population[np.random.choice(range(len(population)), p=fitnesses/np.sum(fitnesses))]
        parent2 = population[np.random.choice(range(len(population)), p=fitnesses/np.sum(fitnesses))]
        parent1 = bin(parent1)[2:].zfill(5)
        parent2 = bin(parent2)[2:].zfill(5)
        #print(parent1,parent2)
        child1, child2 = crossover(parent1, parent2)
        #print(child1,child2)
        #next_population.append(mutation(child1))
        #next_population.append(mutation(child2))
        next_population.append(int(child1, 2))
        next_population.append(int(child2,2))
    return next_population    

def genetic_algorithm(population_size, generations):
    population = generate_population(population_size)
    for i in range(generations):
        print('--------------------------------------------------------------------------------------------------------------------')
        print(f'--------------------------------Generation: {i+1}-----------------------------------------------------------------------')
        #print(f'Generation: {i}')
        fitness_values = calculate_fitness(population)
        print(f'Sum: {sum(fitness_values)}')
        print(f'Avg: {sum(fitness_values)/len(fitness_values)}')
        print(f'Max: {max(fitness_values)}')
        selection_probability_values = selection_probability(fitness_values)  #g(x)
        selected_population = get_next_generation(population, fitness_values)
        population = selected_population
        print(f'selected_new_population: {selected_population}')
        #print(f'Maximum: {max(calculate_fitness(population))}')
    return max(calculate_fitness(population))

if __name__ == "__main__":
    a = int(input('population_size:'))
    b = int(input('generation:'))
    result = genetic_algorithm(a, b)
    print("The maximum of the function on the interval [0, 31] is:", result)