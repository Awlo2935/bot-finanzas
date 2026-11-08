import sqlite3
from flask import Flask, request

app = Flask(__name__)


def consultar_db(query, params=()):
  conn = sqlite3.connect("finanzas.db")
  cursor = conn.cursor()
  cursor.execute(query, params)
  resultado = cursor.fetchall()
  conn.close()
  return resultado


@app.route("/")
def home():
  return "¡El bot de finanzas está activo y funcionando al pelo!"


@app.route("/bot", methods=["POST"])
def bot():
  mensaje_recibido = request.form.get("Body", "").strip().lower()

  if "resumen" in mensaje_recibido:
    # Consultar saldos rápidos
    efectivo = 106.00
    calle = 968.50
    alquiler = 50.00
    respuesta = (
        f"📊 *Tu Balance Actual*\n- Efectivo en mano: ${efectivo:.2f}\n-"
        f" Alquiler restante: ${alquiler:.2f}\n- Total en la calle:"
        f" ${calle:.2f}"
    )
  elif "cobré" in mensaje_recibido or "cobro" in mensaje_recibido:
    respuesta = (
        "✅ ¡Movimiento registrado! (Recuerda actualizar tu base de datos)."
    )
  else:
    respuesta = (
        "🤖 ¡Hola, hermano! Escribe *Resumen* para ver tus cuentas al día."
    )

  return str(respuesta)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)