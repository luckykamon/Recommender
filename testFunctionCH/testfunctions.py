import pandas as pd
import pickle
import matplotlib.pyplot as plt
from main import load_data
from main import get_turnover_per_cat
from main import get_list_column_no_duplicate
import json

# Load the pkl file into a DataFrame
df = pd.read_pickle("../Project_data/data.pkl")

def top10_product(df):
    # Count the occurrences of each product id
    counts = df['LIBELLE'].value_counts()

    # Sort the counts in descending order
    counts = counts.sort_values(ascending=False)

    # Retrieve the top 10 most frequently occurring product ids
    top_10 = counts.head(10)

    # Create a new DataFrame to store the results
    results_df = pd.DataFrame(columns=['LIBELLE', 'QUANTITE', 'CA'])

    # Iterate over the top 10 products
    for product_id, count in top_10.iteritems():
        # Get the price of the product
        price = df.loc[df['LIBELLE'] == product_id, 'PRIX_NET'].iloc[0]
        # Calculate the turnover for the product
        turnover = count * price
        # truncate turnover variable for it to be integer
        turnover = int(turnover)

        # Add the results to the DataFrame
        results_df = results_df.append({'LIBELLE': product_id, 'QUANTITE': count, 'CA': turnover}, ignore_index=True)

    print(results_df)
    # Save the results to a new pkl file
    results_df.to_csv("../Project_data/top10Product.csv", index=False, sep=';', encoding='utf-8')

def get_top10_turnover(df):
    # Group the dataset by the 'LIBELLE' column
    grouped_df = df.groupby(['LIBELLE']).agg({'PRIX_NET': ['sum'], 'TICKET_ID': ['count']})
    # truncate prixt_net : [sum]
    grouped_df['PRIX_NET'] = grouped_df['PRIX_NET'].astype(int)

    # Reset the index and rename columns
    grouped_df.columns = ['turnover', 'quantity']
    grouped_df.reset_index(inplace=True)

    # Sort the dataset by the 'turnover' column in descending order
    grouped_df = grouped_df.sort_values(by='turnover', ascending=False)

    # Select the top 10 rows
    grouped_df = grouped_df.head(10)

    # Export the resulting dataset to a csv file
    grouped_df.to_csv('../Project_data/top10Turnover.csv', index=False, sep=';', encoding='utf-8')
    print("done")


def get_repartition_famille(df):
    # Group the dataset by the 'LIBELLE' column
    grouped_df = df.groupby(['FAMILLE']).agg({'PRIX_NET': ['sum'], 'TICKET_ID': ['count']})
    # truncate prixt_net : [sum]
    grouped_df['PRIX_NET'] = grouped_df['PRIX_NET'].astype(int)

    # Reset the index and rename columns
    grouped_df.columns = ['turnover', 'quantity']
    grouped_df.reset_index(inplace=True)

    # Sort the dataset by the 'turnover' column in descending order
    grouped_df = grouped_df.sort_values(by='turnover', ascending=False)

    # Export the resulting dataset to a csv file
    grouped_df.to_csv('../Project_data/repartitionFamille.csv', index=False, sep=';', encoding='utf-8')
    print("done")

get_repartition_famille(df)