import sqlite3

conn = sqlite3.connect('finanzas.db')
cursor = conn.cursor()
cursor.execute(
    'CREATE TABLE IF NOT EXISTS cuentas (id INTEGER PRIMARY KEY, concepto TEXT,'
    ' monto REAL)'
)
conn.commit()
conn.close()