import pandas as pd
import matplotlib.pyplot as plt

# Load Data and calculate the average price for each year
df = pd.read_csv('breadprice.csv')
df['Average Price'] = df[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']].mean(axis=1)

# Display dataset with Average Price
print("\nOutput:")
print(df)

# Display Year and Average Price
print("\nYear and Average Price:")
print(df[['Year', 'Average Price']])

# Generate the graph
plt.figure(figsize=(10,5))
plt.plot(df['Year'], df['Average Price'], marker='o', label='Average Price')
plt.title('Average Price of Bread Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.legend()
plt.grid(True)
plt.show()
