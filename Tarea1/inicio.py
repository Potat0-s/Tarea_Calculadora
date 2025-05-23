from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def inicio():
    valor1 = request.form.get('valor1', '')
    valor2 = request.form.get('valor2', '')
    activo = request.form.get('activo', 'valor1')
    resultado = ''

    if request.method == 'POST':
        # Si se presiona un número
        if 'numero' in request.form:
            numero = request.form['numero']
            if activo == 'valor1':
                valor1 += numero
            else:
                valor2 += numero

        # Si se presiona una operación
        elif 'operacion' in request.form:
            try:
                n1 = float(valor1) if valor1 else 0
                n2 = float(valor2) if valor2 else 0
                op = request.form['operacion']
                if op == '+':
                    resultado = n1 + n2
                elif op == '-':
                    resultado = n1 - n2
                elif op == '*':
                    resultado = n1 * n2
                elif op == '/':
                    resultado = n1 / n2 if n2 != 0 else 'Error'
                elif op == 'raiz':
                    resultado = n1 ** 0.5 if activo == 'valor1' else n2 ** 0.5
                elif op == 'cuadrado':
                    resultado = n1 ** 2 if activo == 'valor1' else n2 ** 2
            except Exception:
                resultado = 'Error'

        # Si se presiona borrar
        elif 'accion' in request.form and request.form['accion'] == 'borrar':
            valor1 = ''
            valor2 = ''
            resultado = ''

    return render_template('inicio.html', valor1=valor1, valor2=valor2, activo=activo, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)