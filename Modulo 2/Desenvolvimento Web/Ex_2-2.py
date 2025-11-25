from flask import Flask, render_template  # Importando Ferramentas

app = Flask(__name__) # Cria app Flask

@app.route('/') # Decorador de Função
def index(): # Função da Rota
    return render_template('ex_2-2.html') # Retorna Para o Site(Navegador)


@app.route('/sobre') # Decorador de Função
def sobre(): # Função da Rota
    return 'Lucas aluno de python e js' # Retorna Para o Site(Navegador)


@app.route('/saudacao/<nome>') # Decorador de Função
def saudacao(nome): # Função da Rota
    return f'Olá {nome}' # Retorna Para o Site(Navegador)


@app.route('/dobro/<int:numero>') # Decorador de Função
def dobro(numero): # Função da Rota
    return f'O dobro de {numero} é: {numero*2}' # Retorna Para o Site(Navegador)





# Rodar o Flask direto
if __name__ == '__main__':  
    app.run(debug=True)