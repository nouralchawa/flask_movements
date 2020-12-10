from movements import app
from flask import render_template, request, url_for, redirect
import csv
import sqlite3

@app.route('/')
def listaIngresos():
    conn = sqlite3.connect('movements/data/lista.db')
    c = conn.cursor()

    c.execute('SELECT fecha, concepto, cantidad, id FROM movimientos;')
    
    '''
    fIngresos = open("movements/data/basedatos.csv","r")
    csvReader = csv.reader(fIngresos, delimiter=',',quotechar='"')
    ingresos =list(csvReader)
    '''
    ingresos = c.fetchall()

    total = 0
    for ingreso in ingresos:
        total += float(ingreso [2])

    conn.close()

    return render_template("movementsList.html", datos=ingresos, total=total)

@app.route('/creaalta', methods=['GET','POST'])
def nuevoIngreso():
    if request.method == 'POST':
        conn = sqlite3.connect('movements/data/lista.db')
        c = conn.cursor()

        c.execute('INSERT INTO movimientos(cantidad, concepto, fecha) VALUES(?,?,?);',
                (
                    float(request.form.get('cantidad')),
                    request.form.get('concepto'),
                    request.form.get('fecha')
                )
        )

        conn.commit()


        '''
        fIngresos = open("movements/data/basedatos.csv","a", newline="")
        csvWriter = csv.writer(fIngresos, delimiter=',', quotechar='"')
        csvWriter.writerow([request.form.get('fecha'), request.form.get('concepto'), request.form.get('cantidad')])
        '''
        return redirect(url_for('listaIngresos'))
        

        conn.close()

    return render_template("alta.html")

@app.route("/modifica/<id>", methods=['GET','POST'])
def modificaIngresos(id):
    '''
        1.Consulta el movimiendo por id
        2. render_template(modifica.html, movimiento=el resultado de la consulta anterior)
        update movimientos set concepto ="Extra de navidad" where id=4
        delete from movimientos where id=5
    '''
