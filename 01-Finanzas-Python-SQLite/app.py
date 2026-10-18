import sqlite3

# 1. Conectar a la base de datos (crea el archivo finanzas.db automáticamente)
conexion = sqlite3.connect("finanzas.db")
cursor = conexion.cursor()

# 2. Crear la tabla de gastos con SQL si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS gastos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        concepto TEXT NOT NULL,
        monto REAL NOT NULL,
        categoria TEXT NOT NULL
    )
""")

# 3. Función para guardar un gasto en la base de datos
def agregar_gasto(concepto, monto, categoria):
    cursor.execute("INSERT INTO gastos (concepto, monto, categoria) VALUES (?, ?, ?)", 
                   (concepto, monto, categoria))
    conexion.commit()
    print(f"✅ Gasto registrado: {concepto} por ${monto:,.0f} COP")

# 4. Función para consultar todos los gastos (SQL SELECT)
def mostrar_gastos():
    cursor.execute("SELECT * FROM gastos")
    registros = cursor.fetchall()
    
    print("\n--- 📊 HISTORIAL DE GASTOS EN BASE DE DATOS ---")
    for gasto in registros:
        print(f"ID: {gasto[0]} | Concepto: {gasto[1]} | Monto: ${gasto[2]:,.0f} | Categoría: {gasto[3]}")
    print("------------------------------------------------\n")

# --- REGISTROS DE PRUEBA ---
agregar_gasto("Corte de cabello", 25000, "Personal")
agregar_gasto("Almuerzo Universidad", 15000, "Comida")

# Mostramos la información consultada
mostrar_gastos()

# Cerrar la conexión
conexion.close()