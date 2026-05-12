trayecto_inicio = 0

def welcome():
    print(
    """
    Bienvenide al programa")
    """
    )

def display_opciones():
    print(
    """
    1. Información de tarifas
    2. Empezar un trayecto
    3. Pausar un trayecto
    4. Reaundar un trayecto
    5. Finalizar un trayecto
    """
    )

def opciones():
    elige_opcion = input("Introduce un número del 1 al 5")
    if '1' in elige_opcion:
        print(
        f"""
        Has elegido el número:  {elige_opcion}
        Las tarifas son:
        - Taxi parado = 2 céntimos por segundo.
        - Taxi en marcha = 5 céntimos por segundo.
        """
        )
        print(input("Introduce 2 para empezar el trayecto, 3 para reanudarlo o 4 para finalizarlo "))

    elif '2' in elige_opcion:
        print(
            f"""
            Has elegido el número:  {elige_opcion}
            '¡Comenzamos!')
            """
        )
        return trayecto_inicio
    elif '3' in elige_opcion:
        print(
            f"""
           Has elegido el número:  {elige_opcion} 
            '¡Reaudando trayecto!')
            """
        )
    elif '4' in elige_opcion:
        print(
            f"""
            Has elegido el número:  {elige_opcion} 
            'Trayecto reanudado. Llevas acumulado: x '
            """
        )
    elif '5' in elige_opcion:
        print(
            f"""
            Has elegido el númerp: {elige_opcion}
            'Trayecto finalizado. El precio es: precio')
            """
        )
def calcula(tiempo_parado, tiempo_marcha):
    precio_final = 0.002 * tiempo_parado + 0.005 * tiempo_marcha

#_____________________________________________________
# Hasta aquí funciona, probado test
#______________________________________________________

def fin(precio):

    print(f"Trayecto finalizado. El precio final es: {precio}")


welcome()
display_opciones()
opciones()


