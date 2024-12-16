import random


POPULATION_SIZE = 10
GENE_LENGTH = 5
MUTATION_RATE = 0.1
GENERATIONS = 20


def fitness_function(individual):
    decimal_value = int("".join(map(str, individual)), 2)
    return decimal_value ** 2


def generate_individual():
    return [random.randint(0, 1) for _ in range(GENE_LENGTH)]


def generate_population():
    return [generate_individual() for _ in range(POPULATION_SIZE)]


def selection(population, fitness):
    tournament = random.sample(list(zip(population, fitness)), k=3)
    return max(tournament, key=lambda x: x[1])[0]


def crossover(parent1, parent2):
    point = random.randint(1, GENE_LENGTH - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


def mutate(individual):
    return [gene if random.random() > MUTATION_RATE else 1 - gene for gene in individual]


def genetic_algorithm():
    population = generate_population()

    for generation in range(GENERATIONS):
        fitness = [fitness_function(individual) for individual in population]
        best_individual = population[fitness.index(max(fitness))]
        best_value = int("".join(map(str, best_individual)), 2)
        print(f"Generation {generation}: Best Value = {best_value}, Fitness = {max(fitness)}")


        new_population = []
        while len(new_population) < POPULATION_SIZE:
            parent1 = selection(population, fitness)
            parent2 = selection(population, fitness)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))

        population = new_population[:POPULATION_SIZE]


    fitness = [fitness_function(individual) for individual in population]
    best_individual = population[fitness.index(max(fitness))]
    best_value = int("".join(map(str, best_individual)), 2)
    return best_value, max(fitness)

if __name__ == "__main__":
    solution, fitness = genetic_algorithm()
    print(f"Best solution found: {solution}, Fitness: {fitness}")
