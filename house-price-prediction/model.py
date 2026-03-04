# Import required libraries
import pandas as pd
from sklearn.linear_model import LinearRegression

# Create a simple sample dataset
data = {
    "size": [1000, 1500, 2000, 2500, 3000],   # Size of house in square feet
    "price": [200000, 300000, 400000, 500000, 600000]  # Price of house
}

# Convert dataset into a pandas DataFrame
df = pd.DataFrame(data)

# Define features (input) and target (output)
X = df[["size"]]   # Feature: house size
y = df["price"]    # Target: house price

# Create the Linear Regression model
model = LinearRegression()

# Train the model using the dataset
model.fit(X, y)

# Predict the price of a new house
new_size = [[2200]]   # Example: house with 2200 square feet
predicted_price = model.predict(new_size)

# Print the predicted house price
print("Predicted house price:", predicted_price[0])
