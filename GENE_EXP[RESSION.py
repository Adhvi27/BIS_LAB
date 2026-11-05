import random

# Generate a random gene
def generate_gene():
    return random.randint(1, 10)

# Calculate fitness
def fitness(gene):
    return gene ** 2

# Generate population
population = [generate_gene() for _ in range(6)]

print("Initial Population:", population)

# Gene expression
expressed = [fitness(gene) for gene in population]

print("Gene Expression:", expressed)

# Find the best gene
best_gene = population[expressed.index(max(expressed))]

print("Best Gene:", best_gene)
print("Best Fitness:", fitness(best_gene))
