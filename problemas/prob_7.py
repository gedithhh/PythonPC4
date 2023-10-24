import requests
import sqlite3

url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'

# Conectamos al sitio
response = requests.get(url)

# Verificamos que la conexión al sitio fue exitosa (código 200)
if response.status_code == 200:
    # 2. Recuperamos la información en formato JSON
    data = response.json()

    # Nos conectamos a la base de datos
    with sqlite3.connect('base.db') as conexion:
        sentencia_cursor = conexion.cursor()

        sentencia_cursor.execute('''
            CREATE TABLE IF NOT EXISTS sunat_info (
                fecha TEXT PRIMARY KEY,
                compra REAL,
                venta REAL
            )
        ''')

        # Accedemos a los datos correctos en 'data' (asumiendo que los datos están en una clave llamada 'result')
        tipo_cambio = data.get('result', {})

        for fecha, valores in tipo_cambio.items():
            sentencia_cursor.execute('''
                INSERT OR REPLACE INTO sunat_info (fecha, compra, venta)
                VALUES (?, ?, ?)
            ''', (fecha, valores.get('Compra', 0), valores.get('Venta', 0)))

        conexion.commit()

        # Mostramos el contenido de la tabla 'sunat_info'
        sentencia_cursor.execute('SELECT * FROM sunat_info')
        filas = sentencia_cursor.fetchall()

        for fila in filas:
            print(f"Fecha: {fila[0]}, Compra: {fila[1]}, Venta: {fila[2]}")

    print("Los datos se almacenaron")
else:
    print("Error al obtener datos de la API")
