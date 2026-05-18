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

def start():
    inicio = input("Introduce 'Empezar' para iniciar el trayecto")

    if 'Empezar' in inicio:
        print("""
        ¡Comenzamos!)
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
    input("Introduce 'Finalizar' para terminar el trayecto")
    precio_final = (0.002 * sum(acumulado_parado)) + (0.005 * sum(acumulado_marcha))
    print(f"""
    ¡Trayecto finalizado! El precio es: {precio_final} €
    """
          )

def restart():
    nuevo_trayecto = input("Introduzca 'Empezar' para comenzar un nuevo trayecto")
    if 'Empezar' in nuevo_trayecto:
        welcome()

welcome()
start()
calculate()
finish()
restart()

