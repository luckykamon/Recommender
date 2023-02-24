from functools import lru_cache
from .common import load_data

# CategorieName: Doit renvoyer {"1":"0","2":"0" ... "12":"0"} si la colonne n'existe pas ou mal écrit ou valeur absurde
# Renvoie {"1":"0","2":"0" ... "12":"0"} si la colonne n'existe pas ou mal écrit ou valeur absurde
# Doit renvoyer une valeur pour chaque mois (un entier sous forme de string) pour valeur des décimales sous forme de string, valeurs positives
@lru_cache(maxsize=None)
def get_Turnover_per_Cat(CategorieName, CategorieValue):
    # load data
    data = load_data()
    # create a new dataframe with only the data of the given famille
    data = data[data[CategorieName] == CategorieValue]
    # create a new dataframe with only the columns we need
    data = data[[CategorieName, 'MOIS_VENTE', 'PRIX_NET']]
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
    print(result)
    # convert the list to json
    resJSON = {}
    for element in range(len(result)):
        resJSON[int(result[element][0])] = result[element][1]
    for i in range(1, 13):
        if i not in resJSON:
            resJSON[i] = 0
    return resJSON
