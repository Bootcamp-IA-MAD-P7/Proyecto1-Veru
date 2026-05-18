import time

taxi_parado = True
acumulado_parado = []
acumulado_marcha = []


def welcome():
    print(
    """
    Bienvenide al programa
    Las tarifas son:
    - Taxi parado = 2 céntimos por segundo.
    - Taxi en marcha = 5 céntimos por segundo.
    """
    )


def calculate():
    if taxi_parado == True:
        start_time_parado = time.time()
        end_time_parado = time.time()
        tiempo_parado = end_time_parado - start_time_parado

        acumulado_parado.append(tiempo_parado)
        return acumulado_parado

    if taxi_parado == False:
        start_time_marcha = time.time()
        end_time_marcha = time.time()
        tiempo_marcha = end_time_marcha - start_time_marcha
        acumulado_marcha.append(tiempo_marcha)
        return acumulado_marcha

def finish():
    trayecto_finalizado = input("Introduce 'Finalizar' para terminar el trayecto")
    precio_final = (0.002 * sum(acumulado_parado)) + (0.005 * sum(acumulado_marcha))
    while 'Finalizar' in trayecto_finalizado:
        print(f"""
        ¡Trayecto finalizado! El precio es: {precio_final} €
        """
          )
    while not 'Finalizar' in trayecto_finalizado:
        input("Debes escribir la palabra 'Finalizar'")

def restart():
    nuevo_trayecto = input("Introduzca 'Empezar' para comenzar un nuevo trayecto")
    while 'Empezar' in nuevo_trayecto:
        welcome()
    while not 'Empezar' in nuevo_trayecto:
        input("Debes escribir la palabra 'Empezar'")


def main():
    welcome()
    inicio = input("Introduce 'Empezar' para iniciar el trayecto")

    while 'Empezar' in inicio:
        print("""
        ¡Comenzamos!)
        """
              )
        calculate()
        finish()
        restart()
    while not 'Empezar' in inicio:
        input("Debes escribir la palabra 'Empezar'")