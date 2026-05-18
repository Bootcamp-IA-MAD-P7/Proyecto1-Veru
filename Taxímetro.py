import time
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

taxi_parado = True
acumulado_parado = []
acumulado_marcha = []


def menu():
    print(
    """
    ¡Bienvenide a TaxiVeru!
    Estás en el menú principal.
    Las opciones disponibles son:
    - Empezar: Inicia un trayecto
    - Finalizar: Termina y ve el precio final
    - Reiniciar: Vuelve al menú principal y empieza un nuevo trayecto
    
    Las tarifas disponibles son:
    - Taxi parado = 2 céntimos por segundo.
    - Taxi en marcha = 5 céntimos por segundo.
    """
    )

def start():
    print("""
    ¡Comenzamos!)
    """
          )

def calculate():
    if taxi_parado:
        start_time_parado = time.time()
        end_time_parado = time.time()
        tiempo_parado = end_time_parado - start_time_parado
        acumulado_parado.append(tiempo_parado)

    if not taxi_parado:
        start_time_marcha = time.time()
        end_time_marcha = time.time()
        tiempo_marcha = end_time_marcha - start_time_marcha
        acumulado_marcha.append(tiempo_marcha)

def finish():
    trayecto_finalizado = input("Introduce 'Finalizar' para terminar el trayecto")
    precio_final = (0.002 * sum(acumulado_parado)) + (0.005 * sum(acumulado_marcha))


    while 'Finalizar' in trayecto_finalizado or 'finalizar' in trayecto_finalizado:
        print(f"""
        ¡Trayecto finalizado! El precio es: {precio_final} €
        """
          )
        return restart()

    else:
       logging.error("Escribiste mal la palabra, debes escribir la palabra 'Empezar'. Inténtalo de nuevo")
       start(), calculate(), finish(), restart()
       return finish()

def restart():
    nuevo_trayecto = input("Introduce 'Reiniciar' para volver al menú principal")
    while 'Reiniciar' in nuevo_trayecto or 'reiniciar' in nuevo_trayecto:
        return main()
    else:
        logging.error("Escribiste mal la palabra. Debes escribir la palabra 'Reiniciar'. Inténtalo de nuevo")
        return restart()


def main():
    menu()
    inicio = input("Introduce 'Empezar' para iniciar el trayecto")

    while 'Empezar' in inicio or 'empezar' in inicio:
        start(), calculate(), finish(), restart()


    while not 'empezar' in inicio or not 'Empezar' in inicio:
        logging.error("Escribiste mal la palabra, debes escribir la palabra 'Empezar'. Inténtalo de nuevo")
        main()

main()