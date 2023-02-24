import pandas as pd
from sklearn.neighbors import NearestNeighbors
import time as time
# Load data from pickle file
df = pd.read_pickle('../Project_data/data.pkl')

# Select the first 100 000 rows
df = df.head(100000)

# Save the first 100 000 rows of the dataframe to a new pickle file
df.to_pickle('../Project_data/small.pkl')

# add time to the function to detect what is the bottleneck


# Load data from pkl file
t1 = time.time()
data = pd.read_pickle("../Project_data/small.pkl")
t2 = time.time()
print('read pickle Time: %2.2f sec' % (t2 - t1))

# Create a NearestNeighbors model
t1 = time.time()
nn = NearestNeighbors(n_neighbors=10, algorithm='brute', metric='cosine')
t2 = time.time()
print('narest neighbors model setup Time: %2.2f sec' % (t2 - t1))

# One-hot encode the product IDs
t1 = time.time()
data_encoded = pd.get_dummies(data, columns=['LIBELLE'])
t2 = time.time()
print('encoding Time: %2.2f sec' % (t2 - t1))

# Fit the model on the data
t1 = time.time()
nn.fit(data_encoded[data_encoded.filter(regex='CLI_ID|LIBELLE_|TICKET_ID').columns])
t2 = time.time()
print('fit model Time: %2.2f sec' % (t2 - t1))


def recommend_product(client_id):
    # Check if the client_id exists in the dataset
    t1 = time.time()
    if data_encoded.query("CLI_ID == @client_id").empty:
        return "Error: client id not found in the dataset"
    t2 = time.time()
    print('check client id existing Time: %2.2f sec' % (t2 - t1))


    # Find the 10 most similar clients to the input client
    t1 = time.time()
    distances, indices = nn.kneighbors(
        data_encoded[data_encoded['CLI_ID'] == client_id].filter(regex='CLI_ID|LIBELLE_|TICKET_ID'))
    similar_clients = data_encoded.iloc[indices[0]]
    t2 = time.time()
    print('find 10 most similar clients Time : %2.2f sec' % (t2 - t1))

    # Check if there are similar clients
    if len(similar_clients) == 0:
        return "No recommendations available for this client"

    n = 1  # Number of products to recommend
    # Find the products that the similar clients have purchased but the input client has not
    t1 = time.time()
    recommended_products = data[
        data['CLI_ID'].isin(similar_clients['CLI_ID']) & ~data['CLI_ID'].isin([client_id])].groupby(
        ['CLI_ID', 'LIBELLE']).size().reset_index(name='counts')
    recommended_products = recommended_products.sort_values(by='counts', ascending=False)
    t2 = time.time()
    print('Recommendation Time : %2.2f sec' % (t2 - t1))

    if recommended_products.empty:
        return "No recommendations available for this client"

    return recommended_products.head(n)


print(recommend_product(13290776))
# Example of a client working well with the first 10000 rows :
# print(recommend_product(1490281))

# Example of a client not similar to any other client for the 10000 rows version :
# print(recommend_product(69813934))
