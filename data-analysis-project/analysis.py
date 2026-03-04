import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data.csv")

# Show dataset
print(data)

# Plot sales trend
plt.plot(data["Month"], data["Sales"])
plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
