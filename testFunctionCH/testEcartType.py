from statistics import stdev

import pandas as panda
import pickle
import matplotlib.pyplot as plt
from main import load_data
import json

data = load_data()


def defined_data(origin_data, list_group_by, values):
    result = origin_data.groupby(list_group_by)[values].sum()
    return result


dataFamille = defined_data(data, ['MAILLE', 'MOIS_VENTE'], 'PRIX_NET')
listFamille = data['MAILLE'].unique().tolist()
deviationList = {}
meanCA = []

for famille in listFamille:
    meanCA.append(dataFamille[famille].sum())

meanCA = sum(meanCA) / len(meanCA)

for famille in listFamille:
    if dataFamille[famille].values.size > 1:
        if dataFamille[famille].values.sum() > (0.5 * meanCA):
            deviationList[famille] = (100 * stdev(dataFamille[famille].values.tolist())) / (
                dataFamille[famille].values.sum())

deviationList = dict(sorted(deviationList.items(), key=lambda item: item[1], reverse=True))
print(deviationList)

