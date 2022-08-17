# coding: utf-8
from flask import Flask, render_template, request
app = Flask("projeto")

'''@app.route("/")
def ola_mundo():
    return "Olá Mundo! Esse é o meu primeiro projeto Flask!!", 200'''

#Rota raiz
@app.route("/")
def index():
    nome = "Lamim"
    produto = "PlayStation"
    array = [{"nome":"PS2","valor":"R$ 1200,00"},{"nome":"PS3","valor":"R$ 2100,00"},{"nome":"PS4","valor":"R$ 4000,00"}]
    return render_template("index.html", p = produto, n = nome, a = array), 200

#Rota simples
@app.route("/teste")
def teste():
    return 'Nova rota teste', 200

#Rota com variável
@app.route("/teste/<variavel>")
def teste_var(variavel = ''):
    return 'Nova rota teste<br/>Variável {}'.format(variavel), 200

#Rota formulário
@app.route("/form")
def form():
    return render_template("form.html"), 200

#Rote recebe formulário
@app.route("/form_recebe", methods=["GET", "POST"])
def form_recebe():
    if request.method == "POST":
        nome = request.form["nome"]
        sobrenome = request.form["sobrenome"]
        # return "Nome: {}".format(nome)
        return nome + ' ' + sobrenome, 200
    else:
        return 'Chamada GET não suportada', 200

@app.errorhandler(404)
def handle_404(e):
    return 'Erro, esta URL de chamada não existe.', 404

if __name__ == "__main__":
    app.run()