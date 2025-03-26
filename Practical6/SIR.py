# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
Susceptible = 9999
Susceptible_array = [Susceptible]
Infected = 1
Infected_array = [Infected]
Recovered = 0
Recovered_array = [Recovered]
N=10000
beta=0.3
gamma=0.05

for i in range(1000):
    Infected_new=sum(np.random.choice(range(2),Susceptible,p=[1-beta*(Infected/N),beta*(Infected/N)]))
    Recovered_new=sum(np.random.choice(range(2),Infected,p=[1-gamma,gamma]))
    Infected=Infected_new+Infected-Recovered_new
    Recovered=Recovered_new+Recovered
    Susceptible=N-Infected-Recovered
    Susceptible_array.append(Susceptible)
    Infected_array.append(Infected)
    Recovered_array.append(Recovered)

plt.figure(figsize=(6,4),dpi=150)
plt.plot(Susceptible_array, label='susceptible')
plt.plot(Infected_array, label='infected')
plt.plot(Recovered_array, label='recovered')
plt.xlabel('time')
plt.ylabel('Number of people')
plt.title('SIR Model Simulation')
plt.legend()
# plt.savefig("SIR_plot.png", format="png")
plt.show()