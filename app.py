from flask import Flask, render_template, request, jsonify, session
import random

# ==========================================
# CONFIGURACIÓN GENERAL
# ==========================================

app = Flask(__name__)

# Necesario para guardar datos entre peticiones
app.secret_key = "python_arcade_2026"

# Opciones del juego Piedra Papel Tijera
opciones = ["Piedra", "Papel", "Tijera"]


# ==========================================
# FUNCIÓN PARA DETERMINAR GANADOR
# ==========================================

def determinar_ganador(jugador, maquina):

    if jugador == maquina:
        return 0

    if (
        (jugador == "Piedra" and maquina == "Tijera")
        or (jugador == "Papel" and maquina == "Piedra")
        or (jugador == "Tijera" and maquina == "Papel")
    ):
        return 1

    return 2


# ==========================================
# MENÚ PRINCIPAL
# ==========================================

@app.route("/")
def inicio():
    return render_template("index.html")


# ==========================================
# PIEDRA PAPEL TIJERA
# ==========================================

@app.route("/ppt")
def ppt():
    return render_template("piedra_papel_tijera.html")


@app.route("/jugar", methods=["POST"])
def jugar():

    datos = request.json

    jugador = datos["jugador"]

    maquina = random.choice(opciones)

    resultado = determinar_ganador(
        jugador,
        maquina
    )

    return jsonify({
        "jugador": jugador,
        "maquina": maquina,
        "resultado": resultado
    })


# ==========================================
# ADIVINA EL NÚMERO
# ==========================================

@app.route("/adivina")
def adivina():
    return render_template("adivina_numero.html")


@app.route("/nuevo_juego", methods=["POST"])
def nuevo_juego():

    datos = request.json

    dificultad = datos["dificultad"]

    if dificultad == "facil":
        maximo = 50

    elif dificultad == "normal":
        maximo = 100

    else:
        maximo = 500

    session["numero"] = random.randint(
        1,
        maximo
    )

    session["intentos"] = 0

    return jsonify({
        "maximo": maximo
    })

# ==========================================
# MEMORAMA
# ==========================================

@app.route("/memorama")
def memorama():
    return render_template(
        "memorama.html"
    )

@app.route("/intentar", methods=["POST"])
def intentar():

    datos = request.json

    numero_usuario = int(
        datos["numero"]
    )

    secreto = session["numero"]

    session["intentos"] += 1

    intentos = session["intentos"]

    if numero_usuario == secreto:

        return jsonify({
            "estado": "gano",
            "intentos": intentos
        })

    elif numero_usuario < secreto:

        return jsonify({
            "estado": "mayor"
        })

    else:

        return jsonify({
            "estado": "menor"
        })


# ==========================================
# INICIO DEL SERVIDOR
# ==========================================

""" if __name__ == "__main__":
    #app.run(debug=True)
    app.run(
    host="0.0.0.0",
    port=5000,
    debug=True
) """

if __name__ == "__main__":
    app.run()