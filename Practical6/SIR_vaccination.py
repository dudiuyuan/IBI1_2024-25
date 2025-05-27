import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


# 1.settings
N = 10000                        
initial_infected = 1            
initial_recovered = 0           
beta = 0.3                      
gamma = 0.05                    
time_steps = 1000              # Total simulation time steps
vaccination_rates = [i / 10 for i in range(11)]  # 0% to 100% in 10% steps

# 2.function
def run_simulation(vaccinated_ratio):
    V = int(N * vaccinated_ratio)                                 # Vaccinated individuals
    S = max(N - initial_infected - initial_recovered - V, 0)      # Susceptible population
    I = initial_infected
    R = initial_recovered

    S_list = [S]
    I_list = [I]
    R_list = [R]

    for _ in range(time_steps):
        prob_infection = beta * I / N

        # Randomly simulate new infections
        new_infections = np.sum(np.random.choice(
            [0, 1], size=S, p=[1 - prob_infection, prob_infection])) if S > 0 else 0

        # Randomly simulate new recoveries
        new_recoveries = np.sum(np.random.choice(
            [0, 1], size=I, p=[1 - gamma, gamma])) if I > 0 else 0

        # Update S, I, R
        S = max(S - new_infections, 0)
        I = max(I + new_infections - new_recoveries, 0)
        R += new_recoveries

        S_list.append(S)
        I_list.append(I)
        R_list.append(R)

    return I_list


# 3. Plotting results
plt.figure(figsize=(6,4),dpi=150)

for idx, vac_rate in enumerate(vaccination_rates):
    I_curve = run_simulation(vac_rate)
    color = cm.viridis(idx / len(vaccination_rates))  # Color based on vaccination rate
    plt.plot(I_curve, label=f"{int(vac_rate * 100)}%", color=color)

# Plot formatting
plt.xlabel("Time")
plt.ylabel("Number of people")
plt.title("SIR Model with different Vaccination Rates")
plt.legend(title="Vaccination Rate")
plt.tight_layout()
plt.show()
