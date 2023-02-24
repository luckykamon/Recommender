import flask
import flask_cors

from list.cli_id import index as list_cli_id
from list.famille import index as list_famille
from list.libelle import index as list_libelle
from list.maille import index as list_maille
from list.mois_vente import index as list_mois_vente
from list.prix_net import index as list_prix_net
from list.ticket_id import index as list_ticket_id
from list.univers import index as list_univers

from recommandation.cli_id import index as recommandation_cli_id
from recommandation.libelle import index as recommandation_libelle

from turnover.famille import index as turnover_famille
from turnover.libelle import index as turnover_libelle
from turnover.maille import index as turnover_maille
from turnover.univers import index as turnover_univers

from deviation import index as deviation_all

app = flask.Flask("API T-DAT-901")
flask_cors.CORS(app, resources={r'/*': {'origins': '*'}})

# List

@app.route('/list/cli_id', methods=["GET"])
def flask_list_cli_id():
    return list_cli_id.index(), 200

@app.route('/list/famille', methods=["GET"])
def flask_list_famille():
    return list_famille.index(), 200

@app.route('/list/libelle', methods=["GET"])
def flask_list_libelle():
    return list_libelle.index(), 200

@app.route('/list/maille', methods=["GET"])
def flask_list_maille():
    return list_maille.index(), 200

@app.route('/list/mois_vente', methods=["GET"])
def flask_list_mois_vente():
    return list_mois_vente.index(), 200

@app.route('/list/prix_net', methods=["GET"])
def flask_list_prix_net():
    return list_prix_net.index(), 200

@app.route('/list/ticket_id', methods=["GET"])
def flask_list_ticket_id():
    return list_ticket_id.index(), 200

@app.route('/list/univers', methods=["GET"])
def flask_list_univers():
    return list_univers.index(), 200

# Recommandation

@app.route('/recommandation/cli_id/<cli_id>', methods=["GET"])
def flask_recommandation_cli_id(cli_id):
    return recommandation_cli_id.index(cli_id), 200

@app.route('/recommandation/libelle/<libelle>', methods=["GET"])
def flask_recommandation_libelle(libelle):
    return recommandation_libelle.index(libelle), 200

#Turnover

@app.route('/turnover/famille/<famille>', methods=["GET"])
def flask_turnover_famille(famille):
    return turnover_famille.index(famille), 200

@app.route('/turnover/libelle/<libelle>', methods=["GET"])
def flask_turnover_libelle(libelle):
    return turnover_libelle.index(libelle), 200

@app.route('/turnover/maille/<maille>', methods=["GET"])
def flask_turnover_maille(maille):
    return turnover_maille.index(maille), 200

@app.route('/turnover/univers/<univers>', methods=["GET"])
def flask_turnover_univers(univers):
    return turnover_univers.index(univers), 200


# Deviation

@app.route('/deviation/<category>/<topNumber>/<ascdesc>', methods=["GET"])
def deviation(category, topNumber, ascdesc):
    return deviation_all.index(category, topNumber, ascdesc), 200



@app.route('/', methods=["GET"])
def index():
    return ("It works!", 200)





def main():
    app.run(host="0.0.0.0", port=3000, debug=True)


if __name__ == '__main__':
    main()
