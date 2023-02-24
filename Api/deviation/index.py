import json
import sys

sys.path.append('../.')

from functions_common.common import top_deviation_per_category

def index(category, topNumber, ascdesc):
    return json.dumps(top_deviation_per_category(category, topNumber, ascdesc))