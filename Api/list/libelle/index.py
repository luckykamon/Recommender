import json
import sys

sys.path.append('../..')

from functions_common.get_list_column_no_duplicate import get_list_column_no_duplicate

def index():
    return json.dumps(get_list_column_no_duplicate(6))