# read pickle file in Project_data/data.pkl
# and print the content of the first two rows

import pandas as panda
import pickle
import matplotlib.pyplot as plt

from main import create_csv

panda.set_option('display.max_columns', 8)

with open('../Project_data/data.pkl', 'rb') as f:
    data = pickle.load(f)

# print(data.head(2))
#
# # Do the sum of the column 'PRIX_NET' grouped by the column 'FAMILLE' and split by column ('MOIS_VENTE') as columns
# # and print the result
# result = data.groupby(['FAMILLE', 'MOIS_VENTE'])['PRIX_NET'].sum()
# print(result)
#
# # create csv with result
# result.to_csv('output/CA_by_Famille.csv')
#
# # convert series result to dataframe with 'MOIS_VENTE' as index
# result = result.to_frame()
# result = result.reset_index()
#
# # create graph bar with result divided by 'FAMILLE'
# result.pivot(index='MOIS_VENTE', columns='FAMILLE', values='PRIX_NET').plot(kind='bar')
# plt.savefig('./output/test.png')
# plt.show()


result = data.groupby('CLI_ID')['PRIX_NET'].sum()
# get the top 20 CLI_ID
result = result.to_frame()
result = result.reset_index()
result = result.sort_values(by='PRIX_NET', ascending=False)
result = result.head(20)

# get list of the top 20 CLI_ID
list_cli_id = result['CLI_ID'].tolist()

resultFinal = data.groupby(['CLI_ID', 'MOIS_VENTE'])['PRIX_NET'].sum()
#filter resultFinal by list_cli_id
resultFinal = resultFinal.to_frame()
resultFinal = resultFinal.reset_index()
resultFinal = resultFinal[resultFinal['CLI_ID'].isin(list_cli_id)]
resultFinal.to_csv('output/CA_by_Client_Top20.csv')
