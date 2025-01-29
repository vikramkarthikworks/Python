import numpy as np
import matplotlib.pyplot as plt
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
    return np.sum(np.min(distances, axis=1))  # Sum of min distances

# Jaya Algorithm execution
for iteration in range(num_iterations):
    best_index = np.argmin([objective(pop) for pop in population])
    worst_index = np.argmax([objective(pop) for pop in population])
    
    best_solution = population[best_index]
    worst_solution = population[worst_index]

    for i in range(population_size):
        r1, r2 = np.random.rand(), np.random.rand()
        new_solution = population[i] + r1 * (best_solution - abs(population[i])) - r2 * (abs(worst_solution - population[i]))
        new_solution = np.clip(new_solution, 0, area_size)  # Ensure values are within bounds
        
        if objective(new_solution) < objective(population[i]):
            population[i] = new_solution

# Get the best solution after optimization
optimized_edge_nodes = population[np.argmin([objective(pop) for pop in population])]

#  Visualization Code 
plt.figure(figsize=(8, 8))
plt.scatter(sensor_positions[:, 0], sensor_positions[:, 1], c='blue', marker='o', label="IoT Sensors")
plt.scatter(optimized_edge_nodes[:, 0], optimized_edge_nodes[:, 1], c='red', marker='s', s=100, label="Optimized Edge Nodes")

plt.xlabel("X Coordinate (km)")
plt.ylabel("Y Coordinate (km)")
plt.title("Optimized Edge Node Positions in IoT Network (Jaya Algorithm)")
plt.legend()
plt.grid(True)
plt.show()
