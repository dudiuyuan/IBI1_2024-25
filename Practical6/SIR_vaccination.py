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
rate=[0.1,0.2,0.3,0.4,0.5, 0.6, 0.7, 0.8, 0.9, 1]
for a in rate:
    Susceptible = 9999
    Susceptible_array = [Susceptible]
    Infected = 1
    Infected_array = [Infected]
    Recovered = 0
    Recovered_array = [Recovered]
    N=10000
    beta=0.3
    gamma=0.05
    Susceptible=int(N-Susceptible*a)
    Recovered=int(Susceptible*a)
    for i in range(1000):
        Infected_new=sum(np.random.choice(range(2),Susceptible,p=[1-beta*(Infected/N),beta*(Infected/N)]))
        Recovered_new=sum(np.random.choice(range(2),Infected,p=[1-gamma,gamma]))
        Infected=int(Infected_new+Infected-Recovered_new)
        Recovered=int(Recovered_new+Recovered)
        Susceptible=int(N-Infected-Recovered)
        Infected_array.append(Infected)
    plt.plot(Infected_array, label=str(a*10)+'%')
plt.figure(figsize=(6,4),dpi=150)
plt.xlabel('time')
plt.ylabel('Number of people')
plt.title('SIR Model Simulation')
plt.legend()
# plt.savefig("SIR_plot.png", format="png")
plt.show()