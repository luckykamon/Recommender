import json
import sys

sys.path.append('../..')

from functions_common.get_Turnover_per_Cat import get_Turnover_per_Cat

def index(univers):
    return json.dumps(get_Turnover_per_Cat('UNIVERS', univers))