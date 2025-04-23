import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from CSV
dalys_data = pd.read_csv("D:/IBI/IBI1_2024-25/Practical10/dalys-rate-from-all-causes.csv")
# dalys_data = pd.read_csv("../dalys-rate-from-all-causes.csv")

# Show third column (Year) for first 10 rows
print("\nFirst 10 Years:")
print(dalys_data.iloc[0:10, 2])  # 3rd column is index 2

# The 10th year for Afghanistan: 1999
afghanistan_years = dalys_data[dalys_data.Entity == "Afghanistan"].iloc[9, 2]
print("\n10th year for Afghanistan:", afghanistan_years)

# Boolean indexing for DALYs in 1990
dalys_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]
print("\nDALYs in 1990:")
print(dalys_1990)

# Compare UK and France mean DALYs
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data.Entity == "France", ["DALYs", "Year"]]

mean_uk = uk["DALYs"].mean()
mean_france = france["DALYs"].mean()
print("\nMean DALYs - UK:", mean_uk)
print("Mean DALYs - France:", mean_france)
if mean_uk > mean_france:
    print("UK has higher average DALYs than France.")
else:
    print("France has higher average DALYs than UK.")

# Plot UK DALYs over time
plt.figure(figsize=(10,5))
plt.plot(uk.Year, uk.DALYs, 'b+-', label="UK DALYs")
plt.xticks(uk.Year, rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("UK DALYs Over Time")
plt.legend()
plt.tight_layout()
plt.show()

# Q: What countries had DALYs over 650,000 in any year?
high_dalys = dalys_data[dalys_data.DALYs > 650000]
print("\nCountries with DALYs > 650,000:")
print(high_dalys[["Entity", "Year", "DALYs"]].drop_duplicates())