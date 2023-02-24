import json
import sys

sys.path.append('./')

from functions_common.get_list_column_no_duplicate import get_list_column_no_duplicate
from functions_common.get_Turnover_per_Cat import get_Turnover_per_Cat


def list_duplicates(seq):
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    seen_twice = set(x for x in seq if x in seen or seen_add(x))
    # turn the set into a list (as requested)
    return list(seen_twice)


# Test de la fonction get_list_column_no_duplicate

# Le nombre de mois est toujours le même dans une année
assert get_list_column_no_duplicate(1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Test de valeurs non logique
assert get_list_column_no_duplicate(-1) == []
assert get_list_column_no_duplicate(0.5) == []
assert get_list_column_no_duplicate(15) == []
assert get_list_column_no_duplicate("nok") == []

# On vérifie pour les 8 valeurs possibles qu'il n'y a pas de doublons
for i in range(0, 8):
    assert isinstance(get_list_column_no_duplicate(i), list)
    assert list_duplicates(get_list_column_no_duplicate(i)) == []

# Test de la fonction get_Turnover_per_Cat

# Test de valeurs non logique

print("Test back OK")
