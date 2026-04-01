from flask import Flask, render_template, request

#criando obj
app = Flask(__name__) #name = modulo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def form_cadastro():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST'])
def usua_cadastro():
    nome = request.form.get('nome')
    return f'meu cavalo é show papai, {nome}'