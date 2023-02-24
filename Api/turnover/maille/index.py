import json
import sys

sys.path.append('../..')

from functions_common.get_Turnover_per_Cat import get_Turnover_per_Cat

def index(maille):
    return json.dumps(get_Turnover_per_Cat('MAILLE', maille))