import numpy as np
from scipy.spatial.distance import cdist

# Problem parameters
num_sensors = 50  # Number of IoT sensors
num_edge_nodes = 5  # Number of edge nodes
area_size = 100  # Area size (100x100 km)

# Generate random sensor locations
np.random.seed(42)
sensor_positions = np.random.uniform(0, area_size, (num_sensors, 2))

# Jaya Algorithm parameters
num_iterations = 200
population_size = 50

# Initialize population (random edge node positions)
population = np.random.uniform(0, area_size, (population_size, num_edge_nodes, 2))

# Objective function: minimize total distance from sensors to nearest edge node
def objective(edge_nodes):
    distances = cdist(sensor_positions, edge_nodes)  # Compute distances
    min_distances = np.min(distances, axis=1)  # Find the shortest distance for each sensor
    return np.sum(min_distances)  # Minimize total distance

# Jaya Algorithm loop
for iteration in range(num_iterations):
    fitness = np.array([objective(ind) for ind in population])  # Evaluate all solutions
    best_idx = np.argmin(fitness)
    worst_idx = np.argmax(fitness)

    best_solution = population[best_idx]
    worst_solution = population[worst_idx]

    # Update each individual
    for i in range(population_size):
        r1, r2 = np.random.rand(), np.random.rand()
        new_solution = population[i] + r1 * (best_solution - abs(population[i])) - r2 * (worst_solution - abs(population[i]))

        # Ensure solutions remain within bounds
        new_solution = np.clip(new_solution, 0, area_size)

        # Accept new solution if it's better
        if objective(new_solution) < fitness[i]:
            population[i] = new_solution

# Best solution found
best_positions = population[np.argmin([objective(ind) for ind in population])]
print("Optimized Edge Node Positions (Jaya Algorithm):\n", best_positions)
