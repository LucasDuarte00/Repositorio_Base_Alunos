from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Ola mundo!'


@app.route('/sobre')
def sobre():
    return 'Olá eu sou Lucas Duarte, dev em python.'


@app.route('/ola/<nome>')
def ola(nome):
    if nome == 'Lucas':
        return f'Seja bem vindo craque!'
    else:
        return f'Olá {nome}!'



if __name__ == '__main__':
    app.run(debug=True)