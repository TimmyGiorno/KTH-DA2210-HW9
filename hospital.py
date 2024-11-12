"""
Code for KTH DA2210 HW9 Part 2.

Author：Bingchu Zhao (Timmy)
Email：timmyzhao@worldline-ai.cn, bingchu@kth.se
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
lambda_daily = 300
days = 3 * 365

# Simulating.
daily_arrivals = np.random.poisson(lam=lambda_daily, size=days)

# Plotting the results.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Time series of daily arrivals
ax1.plot(daily_arrivals, color='blue')
ax1.axhline(y=369, color='red', linestyle='--', label='Observed: 369 visitors')
ax1.set_title('Daily Arrivals Simulation Over 3 Years')
ax1.set_xlabel('Days')
ax1.set_ylabel('Number of Arrivals')
ax1.legend()

# Histogram of daily arrivals
ax2.hist(daily_arrivals, bins=30, color='lightblue', edgecolor='black')
ax2.axvline(x=369, color='red', linestyle='--', label='Observed: 369 visitors')
ax2.set_title('Histogram of Daily Arrivals')
ax2.set_xlabel('Number of Arrivals')
ax2.set_ylabel('Frequency')
ax2.legend()

plt.tight_layout()
plt.savefig('hospital_result.png')
plt.show()