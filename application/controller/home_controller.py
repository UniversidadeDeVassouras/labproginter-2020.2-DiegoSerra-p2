from application import app
from flask import render_template
from application.model.dao.produto_dao import ProdutoDAO


@app.route("/")
@app.route('/home')
def home():
  produto_dao = ProdutoDAO()
  lista_produtos = produto_dao.listarProduto()
  return render_template('index.html',  lista_produtos= lista_produtos)
#return render_template("index.html")
#@app.route('/')


