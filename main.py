import pandas as panda
import pickle
import matplotlib.pyplot as plt
import os

ProjectDirectory = os.getcwd()

def load_data_with_path(path):
    with open(path, 'rb') as file:
        res = pickle.load(file)
    return res

def load_data():
    with open(ProjectDirectory + '/../Project_data/data.pkl', 'rb') as file:
        res = pickle.load(file)
    return res


def create_csv(origin_data, list_group_by, values, namefile):
    result = origin_data.groupby(list_group_by)[values].sum()
    result.to_csv('output/' + namefile + '.csv')
    print('Done')


def create_graph(csv_file, index, column, values, plot_type, namefile, show):
    df = panda.read_csv(csv_file)
    df = df.reset_index()
    df.pivot(index=index, columns=column, values=values).plot(kind=plot_type)
    plt.savefig('./output/' + namefile + '.png')
    if show:
        plt.show()


def get_list_column_no_duplicate(num_column):
    list_no_duplicate = load_data().iloc[:, num_column].tolist()
    list_no_duplicate = list(dict.fromkeys(list_no_duplicate))
    list_no_duplicate.sort()
    return list_no_duplicate


def get_turnover_per_cat(categorie_name, categorie_value):
    # load data
    data = load_data()
    # create a new dataframe with only the data of the given famille
    data = data[data[categorie_name] == categorie_value]
    # create a new dataframe with only the columns we need
    data = data[[categorie_name, 'MOIS_VENTE', 'PRIX_NET']]
    # group by mois_vente and sum the PRIX_NET
    result = data.groupby(['MOIS_VENTE'])['PRIX_NET'].sum()
    # convert the result to a dataframe
    result = result.to_frame()
    # reset the index
    result = result.reset_index()
    # sort the result by MOIS_VENTE
    result = result.sort_values(by='MOIS_VENTE', ascending=True)
    # make a list from result
    result = result.values.tolist()
    # convert the list to json
    resJSON = {}
    for element in range(len(result)):
        resJSON[result[element][0]] = result[element][1]
    return resJSON



# testing get_list_column_no_duplicate here : ------------------------------
# print(get_list_column_no_duplicate(0))
# ------------------------------------------------------------------------

# testing get_Turnover_per_Cat here : ------------------------------------
# print(get_Turnover_per_Cat('MAILLE', 'CORPS_HYDR_LAIT_HUILE'))
# ------------------------------------------------------------------------


# def create_csv_topx(origin_data, list_group_by, values, namefile, topX):
#     result = origin_data.groupby(list_group_by)[values].sum()
#     result = result.to_frame()
#     result = result.reset_index()
#     result = result.sort_values(by=values, ascending=False)
#     result = result.head(topX)
#     result.to_csv('output/' + namefile + '.csv')
#     print('Done')
