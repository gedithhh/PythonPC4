
import requests

try:
    n = float(input("Ingrese la cantidad de Bitcoins que usted posee: "))

    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    # Verificamos el exito de la olicitud
    if response.status_code == 200:
        data = response.json()
        price_usd = data['bpi']['USD']['rate_float']
        
        # Calculamos el costo actual en USD
        costo_actual_usd = n * price_usd

        print(f"El costo actual es: {costo_actual_usd:,.4f} USD")
    else:
        print("No se pudo obtener el precio de Bitcoin.")
except requests.RequestException as e:
    print(f"Error al realizar la solicitud: {e}")
except ValueError:
    print("Ingrese una cantidad válida de Bitcoins.")
