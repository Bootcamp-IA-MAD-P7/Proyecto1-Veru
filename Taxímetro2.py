def welcome():
    print("""
Bienvenide al programa
1. Información de tarifas
1. Empezar : Introduzca esta opción para empezar un trayecto
2. Reaundar: Introduzca esta opción para pausar un trayecto
4. Finalizar: Introduzca esta opción para finalizar un trayecto
 """)

def prizes():
    elige_opcion = input("Introduce una opción del 1 al 4")
    if '1' in elige_opcion:
        print(
        f"""
        Has elegido el número:  {elige_opcion}
        Las tarifas son:
        - Taxi parado = 2 céntimos por segundo.
        - Taxi en marcha = 5 céntimos por segundo.
        """
        )
    cambio_opcion = input("Introduce el número 0 para volver")
    if '1' in cambio_opcion:
        welcome()


#_____________________________________________________
# Probado hasta aquí
#______________________________________________________



def inicia():
    if input_inicio == 1:
        print('¡Comenzamos!')

def calcula(tiempo_parado, tiempo_marcha):
    precio = 0.002 * tiempo_parado + 0.005 * tiempo_marcha

def fin(precio):
    if
    print(f"Trayecto finalizado. El precio final es: {precio}")


bienvenida()
inicio()
calcula(300,1500)
fin(precio)




