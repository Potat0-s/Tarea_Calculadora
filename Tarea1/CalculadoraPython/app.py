from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    resultado = ''
    valor1 = ''
    operacion = ''
    if request.method == 'POST':
        valor1 = request.form.get('valor1', '')
        operacion = request.form.get('operacion', '')
        resultado = request.form.get('resultado', '')

        # Números
        for i in range(10):
            if f'n{i}' in request.form:
                resultado += str(i)
        if 'n0' in request.form:
            resultado += '0'

        # Operaciones
        if 'nmas' in request.form:
            valor1 = resultado
            operacion = '+'
            resultado = ''
        if 'nmenos' in request.form:
            valor1 = resultado
            operacion = '-'
            resultado = ''
        if 'nmul' in request.form:
            valor1 = resultado
            operacion = '*'
            resultado = ''
        if 'ndiv' in request.form:
            valor1 = resultado
            operacion = '/'
            resultado = ''
        if 'nraiz' in request.form:
            try:
                resultado = str(math.sqrt(float(resultado)))
            except:
                resultado = 'Error'
        if 'npot' in request.form:
            try:
                resultado = str(float(resultado) ** 2)
            except:
                resultado = 'Error'
        if 'nigual' in request.form:
            try:
                if operacion == '+':
                    resultado = str(float(valor1) + float(resultado))
                elif operacion == '-':
                    resultado = str(float(valor1) - float(resultado))
                elif operacion == '*':
                    resultado = str(float(valor1) * float(resultado))
                elif operacion == '/':
                    if float(resultado) == 0:
                        resultado = 'Error'
                    else:
                        resultado = str(float(valor1) / float(resultado))
                valor1 = ''
                operacion = ''
            except:
                resultado = 'Error'
        if 'nclear' in request.form:
            resultado = ''
            valor1 = ''
            operacion = ''

    return render_template('inicio.html', resultado=resultado, valor1=valor1, operacion=operacion)

if __name__ == '__main__':
    app.run(debug=True)
