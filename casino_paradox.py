"""
Code for KTH DA2210 HW9 Part 1.

Author：Bingchu Zhao (Timmy)
Email：timmyzhao@worldline-ai.cn, bingchu@kth.se
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters.
max_payout = 10000000
num_games = 10000
num_simulations = 10

# Function to simulate a single game.
def simulate_game(max_payout):
    payout = 1
    total_payout = 0
    toss_count = 0

    while total_payout + payout <= max_payout:
        toss_count += 1

        if np.random.rand() < 0.5:
            total_payout += payout
            return total_payout
        else:
            payout *= 2

    return max_payout

all_simulations_results = []

for _ in range(num_simulations):
    game_results = [simulate_game(max_payout) for _ in range(num_games)]
    cumulative_avg_payoff = np.cumsum(game_results) / (np.arange(num_games) + 1)
    all_simulations_results.append(cumulative_avg_payoff)

# Calculate the mean convergence curve.
mean_convergence = np.mean(all_simulations_results, axis=0)

# Plotting results.
plt.figure(figsize=(12, 6))
for i, simulation_result in enumerate(all_simulations_results, 1):
    plt.plot(simulation_result, alpha=0.3, label=f'Simulation {i}')
plt.plot(mean_convergence, color='black', linewidth=2, label='Mean Convergence')
plt.xlabel('Number of Games (n)')
plt.ylabel('Average Payoff (SEK)')
plt.title('Average Payoff Convergence for St. Petersburg Paradox Simulation')
plt.legend(loc="upper right")
plt.grid(True)
plt.savefig('casino_paradox_result.png')
plt.show()
