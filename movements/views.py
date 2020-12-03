from movements import app
from flask import render_template
import csv

@app.route('/')
def listaMovimientos():
    fIngresos = open("movements/data/basedatos.csv","r")
    csvReader = csv.reader(fIngresos, delimiter=',',quotechar='"')
    ingresos =list(csvReader)

    sumador = 0
    for ingreso in ingresos:
        sumador += float(ingreso [2])

    print(ingresos)

    return render_template("movementsList.html", datos=ingresos, total=sumador)

@app.route('/creaalta')
def nuevoIngreso():
    return 'Ya el miercoles te enseño el formulario'