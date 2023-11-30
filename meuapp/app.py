from flask import Flask #importante Flask
from flask import render_template #renderiza o html
from flask import request

app = Flask(__name__) #criando um objeto Flask

#Flask é baseado em rotas!

@app.route('/', methods=['GET', 'POST'])  #toda rota deve ta associado a uma função!
def index():
    listaPy = ['Salut Monde', 'Hello World', 'Olá Mundo', 'Eita']

    if 'texto' in request.form: #Ver se algum dado foi enviado no formulário
        listaPy.append(request.form['texto'])

    return render_template('olamundo.html', listaHtml=listaPy)

@app.route('/gilbran')
def ola():
    return "Salut Mondo"

@app.route('/Dia da Semana')
def semana():
    return "<h1>SEG TER QUA QUI SEX SÁB DOM<h1>" 

@app.route('/aula/<int:n>') #<int:n> --> tipo:variável
def aula(n):
    return f"<h1>Aula de número {n}</h1>"