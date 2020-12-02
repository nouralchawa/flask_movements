from movements import app
from flask import render_template

@app.route('/')
def listaMovimientos():
    return render_template("movementsList.html", miTexto="Ya veremos si hay movimientos o no")