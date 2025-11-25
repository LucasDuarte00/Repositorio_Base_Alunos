from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    n = 'Lucas'
    sobrenome = 'Duarte'
    return render_template('ex_3-1.html', nome = n, sobrenome = sobrenome)


if __name__ == '__main__':
    app.run(debug=True)