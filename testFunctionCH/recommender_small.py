import pandas as pd
from sklearn.decomposition import TruncatedSVD
import pickle
specific_client_id = 131204016

# Load data from pickle file
df = pd.read_pickle('../Project_data/data.pkl')

# Select the first 100000 rows
df = df.head(100000)

# Save the first 1000 rows of the dataframe to a new pickle file
df.to_pickle('../Project_data/small.pkl')

# Create pivot table with client ID as rows, product ID as columns, and purchase count as values
pivot_table = df.pivot_table(values='TICKET_ID', index='CLI_ID', columns='LIBELLE', aggfunc='count')



# Replace missing values with 0
pivot_table = pivot_table.fillna(0)

# Create TruncatedSVD instance
svd = TruncatedSVD(n_components=100)
svd_matrix = svd.fit_transform(pivot_table)

# Fit and transform pivot table
pivot_table_svd = svd.fit_transform(pivot_table)

# Create mapping of client ID to index in transformed matrix
client_index_mapping = {client_id: index for index, client_id in enumerate(pivot_table.index)}

# Get index of specific client ID
client_index = client_index_mapping[specific_client_id]

# Get client's row in transformed matrix
client_vector = pivot_table_svd[client_index, :]

# Get dot product of client's row with all other rows
similarities = pivot_table_svd.dot(client_vector)

# Get index of most similar client
most_similar_index = similarities.argmax()

# Get most similar client's ID
most_similar_client = pivot_table.index[most_similar_index]

# Get most similar client's purchase history
most_similar_purchases = pivot_table.loc[most_similar_client, :]

# Get the items that the specific client has not purchased yet
not_purchased = pivot_table.loc[specific_client_id, :] == 0

# Get the items that are in the most_similar_purchases array
items_in_most_similar = pivot_table.columns.isin(most_similar_purchases)

# Slice the not_purchased boolean mask to only select the columns that correspond to the items in the most_similar_purchases array
not_purchased_sliced = not_purchased[items_in_most_similar]

# Get the indices of the most similar items for each item that the client has not purchased
indices = svd_matrix[:, not_purchased_sliced].argsort(axis=1)
# Get the items that the specific client has not purchased yet
not_purchased_items = pivot_table.columns[not_purchased_sliced]
# Get the recommended items
recommended_items = not_purchased_items[indices[:, -1]]
