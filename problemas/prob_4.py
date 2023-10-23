#Ponemos en un diccionario los datos del precio del bitcoin
dic_precios_bitcoin = {
    "USD": 31754.0449,
    "GBP": 26533.4259,
    "EUR": 30933.0758
}

archivo_bit = "precios_bitcoin.txt"

with open(archivo_bit, "w") as file:
    
    file.write("Precios del Bitcoin:\n")
    for currency, price in dic_precios_bitcoin.items():
        file.write(f"{currency}: {price}\n")

print(f"Los datos se  han almacenado correctamente en: '{archivo_bit}'.")

texto = open(f'precios_bitcoin.txt').read()
print(texto)
