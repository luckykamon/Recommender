from functools import lru_cache
from .common import load_data

# Numéro de colonne à tester, ne doit pas crash avec les valeurs suivantes: -1; 0; 1; 0.5; 15; 4; "ok"; true; false
# Vérifier, qu'il n'y a pas de doublons dans la liste retournée
@lru_cache(maxsize=None)
def get_list_column_no_duplicate(num_column):
    if not isinstance(num_column, int) or num_column < 0 or num_column > 7:
        return []
    list_no_duplicate = load_data().iloc[:, num_column].tolist()
    list_no_duplicate = list(dict.fromkeys(list_no_duplicate))
    list_no_duplicate.sort()
    return list_no_duplicate

# print(get_list_column_no_duplicate(1))
