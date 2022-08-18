# coding: utf-8
from flask import Flask, render_template, request, session, redirect, url_for
app = Flask("projeto")
#Criando uma chave de criptografia
app.secret_key = "chave_que_deve_ficar_em_segredo__nao_se_deve_subir_no_git"

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

#Rota form de Login
@app.route("/login")
def login():
    return render_template("login.html"), 200

#Rota de validação de Login
@app.route("/login_validar", methods=["GET", "POST"])
def login_validar():
    if request.method == "POST":
        if request.form["login"] == "lamim" and request.form["senha"] == "aula":
            session["usuario"] = request.form["login"]
            session["codigo"] = 1
            return redirect(url_for("acesso_restrito")) #"logado", 200
        else:
            return "Usuário ou Senha Incorreta", 200
    else:
        if session["usuario"] == "lamim" and session["codigo"] == 1:
            return redirect(url_for("acesso_restrito")) #"logado", 200
        else:
            return "Necessário fazer login", 200

#Rota de acesso restrito (área logado)
@app.route("/restrito")
def acesso_restrito():
    if session["codigo"] == 1:
        return "Bem-vindo à area restrita!!<br>Usuário: {}<br>Código: {}".format(session["usuario"], session["codigo"]), 200
    else:
        return "Acesso inválido!", 200

@app.errorhandler(404)
def handle_404(e):
    return 'Erro, esta URL de chamada não existe.', 404

if __name__ == "__main__":
    app.run()