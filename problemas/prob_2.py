from pyfiglet import Figlet
import random

fuentes_disp = Figlet().getFonts()

fuente = input("Ingrese el nombre de la fuente a usar o en su defecto se asignará alguna fuente random: ")
if not fuente:
    fuente = random.choice(fuentes_disp)

texto_ingresado = input("Ingrese un texto porfavor: ")

figlet = Figlet(font=fuente)

texto_confuente = figlet.renderText(texto_ingresado)
print(texto_confuente)

