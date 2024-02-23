from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)


class CertaBot(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Empresa = db.Column(db.String(50))
    Produtos = db.Column(db.String(50))
    Preco = db.Column(db.Double)
    Tipo = db.Column(db.String(50))
    Imposto = db.Column(db.Double)

    def __init__(self, id, Empresa, Produtos, Preco, Tipo, Imposto):
        self.id = id
        self.Empresa = Empresa
        self.Produtos = Produtos
        self.Preco = Preco
        self.Tipo = Tipo
        self.Imposto = Imposto


@app.route('/')
def index():
    return render_template('http://127.0.0.1:5000')


if __name__ == '__main__':
    app.run(debug=True)
