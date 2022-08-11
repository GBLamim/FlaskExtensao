# coding: utf-8
from flask import Flask, render_template
app = Flask("projeto")

#@app.route("/")
#def ola_mundo():
#    return "Olá Mundo! Esse é o meu primeiro projeto Flask!!", 200

@app.route("/")
def index():
    nome = "Lamim"
    array = [{"nome":"PS2","valor":"R$ 1200,00"},{"nome":"PS3","valor":"R$ 2100,00"},{"nome":"PS4","valor":"R$ 4000,00"}]
    return render_template("index.html", n = nome, a = array), 200

if __name__ == "__main__":
    app.run()