import pandas as panda
import pickle
import matplotlib.pyplot as plt
from statistics import stdev


def load_data():
    with open('Project_data/data.pkl', 'rb') as file:
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


# category is either 'MAILLE', 'FAMILLE', 'UNIVERS', or 'LIBELLE'
def top_deviation_per_category(category, topNumber, ascdesc):
    with open('Project_data/data.pkl', 'rb') as file:
        data = pickle.load(file)
    dataFamille = data.groupby([category, 'MOIS_VENTE'])['PRIX_NET'].sum()
    listFamille = data[category].unique().tolist()
    deviationList = {}
    meanCA = []
    topNumber = int(topNumber)
    if ascdesc == 'true':
        ascdesc = True
    else:
        ascdesc = False


    if topNumber < 1:
        return 0

    for famille in listFamille:
        meanCA.append(dataFamille[famille].sum())

    meanCA = sum(meanCA) / len(meanCA)

    for famille in listFamille:
        if dataFamille[famille].values.size > 1:
            if dataFamille[famille].values.sum() > (0.5 * meanCA):
                deviationList[famille] = (100 * stdev(dataFamille[famille].values.tolist())) / (
                    dataFamille[famille].values.sum())

    deviationList = dict(sorted(deviationList.items(), key=lambda item: item[1], reverse=ascdesc))
    # return the first 3 items of deviationList
    if topNumber > len(listFamille):
        return deviationList
    else:
        return dict(list(deviationList.items())[0:topNumber])


# EXAMPLE testing top 5 Maille :
# Category, topNumber, True for most ecart-type, False for flat values
# print(top_deviation_per_category('MAILLE', 5, True))


