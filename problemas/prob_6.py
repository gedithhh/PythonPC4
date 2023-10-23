import os

def contador_de_lineas_codigo(ruta_archivo):
    try:
        if not ruta_archivo.endswith(".py"):
            print("El archivo es invalido, debe terminar en .py")
            return

        with open(ruta_archivo, 'r') as file:
            lineas = file.readlines()

        lineas_codigo = 0
        comentario = False

        for linea in lineas:
            linea = linea.strip()

            if not comentario:
                if linea.startswith("'''") or linea.startswith('"""'):
                    comentario = True
                elif linea.startswith("#"):
                    continue
                elif linea:
                    lineas_codigo += 1
            else:
                if linea.endswith("'''") or linea.endswith('"""'):
                    comentario = False

        print(f"El archivo tiene {lineas_codigo} líneas de código.")
    except FileNotFoundError:
        print("El archivo no fue encontrado.")

if __name__ == "__main__":

    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contador_de_lineas_codigo(ruta_archivo)
