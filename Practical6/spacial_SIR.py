import numpy as np
import matplotlib.pyplot as plt

# Define parameters
grid_size = 100          
beta = 0.2               
gamma = 0.05             
time_steps = 101   # from 0 to 100 inclusive

# Initialize
population = np.zeros((grid_size, grid_size), dtype=int)
outbreak = np.random.choice(grid_size, size=2)
population[outbreak[0], outbreak[1]] = 1

# Setup plotting
plt.ion()  
fig, ax = plt.subplots(figsize=(6, 4), dpi=150)

# main simulation loop
for t in range(time_steps):
    new_population = population.copy()

    infected_x, infected_y = np.where(population == 1)
    
    for x, y in zip(infected_x, infected_y):

        if np.random.rand() < gamma:
            new_population[x, y] = 2
            continue

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  
                nx, ny = x + dx, y + dy
                if 0 <= nx < grid_size and 0 <= ny < grid_size:
                    if population[nx, ny] == 0 and np.random.rand() < beta:
                        new_population[nx, ny] = 1

    population = new_population

    ax.clear()
    img = ax.imshow(population, cmap='viridis', interpolation='nearest')
    ax.set_title(f"Time step: {t}")
    ax.set_xlabel("X coordinate")
    ax.set_ylabel("Y coordinate")
    plt.pause(0.05)

plt.ioff()
plt.show()

# It was a bit difficult compared to the previous tasks, but I managed to complete it.
# In my initial code, I used several static graphs to display the heatmap for every ten steps. 
# Later, I felt that using animated graphics would be more intuitive, so I modified my code.
# My favorite is the matrix-like model.
# That is, the for loop detection of the people around the infected person is really in line with python.
# That is the most important thing I learned in this task.