import os

path = os.path.dirname(__file__)

# Función para guardar la tabla de multiplicar de un número en un archivo txt
def guardar_en_fichero(n):
    if 1 <= n <= 10:
        nombre_archivo = os.path.join(path, f"tabla-{n}.txt")
        with open(nombre_archivo, "w") as file:
            
            for i in range(1, 13):  # Ahora generamos 12 filas
                file.write(f"{n} x {i} = {n * i}\n")
        print(f"La tabla de multiplicar del {n} se ha guardado en 'tabla-{n}.txt'.")
    else:
        print("El número debe estar entre 1 y 10.")

# Función para mostrar el contenido del archivo
def mostrar_el_fichero(n):
    if 1 <= n <= 10:
        try:
            nombre_archivo =  os.path.join(path, f"tabla-{n}.txt") 
            data = open(nombre_archivo).read()
            print(data)
        except FileNotFoundError:
            print(f"El archivo 'tabla-{n}.txt' no existe.")
    else:
        print("El número debe estar entre 1 y 10.")

#Funcion para mostrar la linea m del fichero

def mostrar_linea_m_del_fichero(n, linea):
    if 1 <= n <= 10:
        try:
            nombre_archivo = os.path.join(path, f"tabla-{n}.txt")
            with open(nombre_archivo, "r") as file:
                lineas = file.readlines()
                if 1 <= linea <= 13:
                    if len(lineas) >= linea:
                        print(f"La linea {linea} es : ")
                        print(lineas[linea - 1])
                    else:
                        print(f"No hay una línea {linea} en 'tabla-{n}.txt'.")
                else:
                    print("El número de línea debe estar entre 1 y 12.")
        except FileNotFoundError:
            print(f"El archivo 'tabla-{n}.txt' no existe.")
    else:
        print("El número debe estar entre 1 y 10.")
# Menú principal
while True:
    print("\nMenú Principal:")
    print("1. Guardar en un fichero la tabla de multiplicar de un número")
    print("2. Mostrar la tabla de multiplicar")
    print("3. Mostrar línea de la tabla de multiplicar")
    print("4. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        numero = int(input("Ingrese un número entre 1 y 10: "))
        guardar_en_fichero(numero)
    elif opcion == "2":
        numero = int(input("Ingrese un número entre 1 y 10: "))
        mostrar_el_fichero(numero)
    elif opcion == "3":
        numero = int(input("Ingrese un número entre 1 y 10: "))
        linea = int(input("Ingrese el número de línea (entre 1 y 12): "))
        mostrar_linea_m_del_fichero(numero, linea)
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    else:
        print("Elija una opción válida")







