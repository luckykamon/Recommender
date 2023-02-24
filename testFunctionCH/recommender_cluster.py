import pandas as pd
from sklearn.neighbors import NearestNeighbors
import time as time
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder
import joblib

number_of_cluster = 200

df = pd.read_pickle("../Project_data/small.pkl")
# On regroupe les données par CLI_ID et LIBELLE
grouped = df.groupby(['CLI_ID', 'LIBELLE']).size().reset_index(name='counts')

# Encodage de la colonne LIBELLE pour pouvoir fit dans le modele
encoder = OneHotEncoder()
one_hot = encoder.fit_transform(grouped[['LIBELLE']])

# ------------ les lignes du bloc à commenter quand c'est déjà run au moins une fois et que le dump est créé
# Fit le modele en le visiant en n cluster (see variable above) en utilisant KMeans
kmeans = KMeans(n_clusters=number_of_cluster)
kmeans.fit(one_hot)

# Save dans le dossier
joblib.dump(kmeans, '../Project_data/kmeans.joblib')
# -----------------fin des lignes à commenter-----------------------------------------------------------

# Load du dossier
kmeans = joblib.load('../Project_data/kmeans.joblib')

# On remet le numero des cluster à chaque groupe de données (on pourra request le numero du cluster pour chaque client)
grouped['cluster'] = kmeans.predict(one_hot)


# function qui retourne le numero de cluster et le produit recommandé pour un client id donné
def get_cluster_and_product(client_id):
    client_data = grouped[grouped['CLI_ID'] == client_id]
    cluster = client_data['cluster'].iloc[0]
    # Ce 'recommender' nous recommande en fait une liste de produit mais on choisi d'en retourner qu'un seul
    # qui est le plus susceptible d'être acheté (parce que c'est le produit acheté le plus fréquemment par les clients de son cluster
    # que lui n'a pas. d'où le [0].
    most_frequent_product = client_data.sort_values('counts', ascending=False).iloc[0:5]['LIBELLE']

    print(f'The client id {client_id} is in the cluster {cluster} and we recommend him to buy : ')
    print(most_frequent_product.iloc[0])
    print(most_frequent_product.iloc[1])
    print(most_frequent_product.iloc[2])
    print(most_frequent_product.iloc[3])
    print(most_frequent_product.iloc[4])


get_cluster_and_product(13290776)
