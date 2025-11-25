from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ex_2-1.html')

@app.route('/sobre')
def sobre():
    return 'Olá eu sou o Lucas. Aluno de Python.'

@app.route('/login')
def login():
    return 'Agora você está logado!'





if __name__ == '__main__':
    app.run(debug=True)