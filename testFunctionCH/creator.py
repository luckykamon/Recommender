import pandas as pd
from sklearn.neighbors import NearestNeighbors
import time as time
# Load data from pickle file
df = pd.read_pickle('../Project_data/data.pkl')

# Select the first 100 000 rows
df = df.head(100000)

# Save the first 100 000 rows of the dataframe to a new pickle file
df.to_pickle('../Project_data/small.pkl')