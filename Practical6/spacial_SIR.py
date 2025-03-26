# population = np.zeros((100,100))

# outbreak =np.random.choice(range(100),2)
# population[outbreak[0],outbreak[1]] = 1
# plt.figure(figsize=(6,4),dpi=150)
# plt.imshow(population, cmap='viridis', interpolation='nearest')

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

size = 100                                          #
population = np.zeros((size, size))
outbreak = np.random.choice(range(size), 2)
population[outbreak[0], outbreak[1]] = 1
beta = 0.3
gamma = 0.05
time_steps = 100


for t in range(time_steps):
    infected = np.argwhere(population == 1)
    new_infections = []
    
    for (i, j) in infected:
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < size and 0 <= nj < size:
                    if population[ni, nj] == 0 and np.random.rand() < beta:
                        new_infections.append((ni, nj))
    
   
    for (i, j) in new_infections:
        population[i, j] = 1
    
    # 恢复过程
    recovery_mask = (population == 1) & (np.random.rand(size, size) < gamma)
    population[recovery_mask] = 2
    
    # 每隔10步绘图
    if t % 10 == 0:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time Step {t}')
        plt.show()