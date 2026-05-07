# Al iniciar, el programa debe dar la bienvenida y explicar su funcionamiento.
from FactoriaF5.prueba import precio_marcha, tiempo_parado


def bienvenida():
    print("""
Bienvenide al programa\n
Tarifa:
 - Taxi parado = 2 céntimos por segundo.
 - Taxi en marcha = 5 céntimos por segundo.

 """)

def inicio():
    print('¡Comenzamos!')

def calcula(tiempo_parado, tiempo_marcha):
    taxi_parado = True

    if taxi_parado == True:
        precio_parado = 0.002 * tiempo_parado
    if taxi_parado == False:
        precio_marcha = 0.005 * tiempo_marcha


precio_parado = 0.002 * tiempo_parado
precio_final = precio_marcha + precio_parado

def fin():

    print(f"Trayecto finalizado. El precio final es: {precio_final}")

bienvenida()
inicio()
calcula(300,1500)
fin()

bienvenida()
inicio()



