
# Program to create Pandas Series with 10 random numbers

import numpy as np
import pandas as pd

# Set seed for fixed random numbers
np.random.seed(42)

# Generate 10 random numbers from 1 to 100
data = np.random.randint(1, 101, 10)

# Display the random numbers
print("Random Numbers:")
print(data)

# Convert numbers into Pandas Series
series = pd.Series(data)

# Display the Pandas Series
print("\nPandas Series:")
print(series)

# Display first value
print("\nFirst Value:", series[0])

# Display last value
print("Last Value:", series[9])

# Display data type
print("Data Type:", series.dtype)

# Display number of values
print("Number of Values:", len(series))
```
