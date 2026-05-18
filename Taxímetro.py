import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

taxi_parado = True
precio_acumulado_parado = []
precio_acumulado_marcha = []


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
    return calculate()

#Marcará 0.0€ en pruebas de pocos segundos por el redondeo

def calculate():
    modo_taxi = input(
        "Escriba '0' si el taxi está parado, '1' si el taxi está moviéndose o 'Finalizar' para terminar el trayecto")
    while modo_taxi == '0':
        start_time_parado = time.time()
        end_time_parado = time.time()
        tiempo_parado = end_time_parado - start_time_parado
        precio_parado = 0.002 * tiempo_parado
        precio_acumulado_parado.append(round(precio_parado, ndigits=2))
        return calculate()

    while modo_taxi == '1':
        start_time_marcha = time.time()
        end_time_marcha = time.time()
        tiempo_marcha = end_time_marcha - start_time_marcha
        precio_marcha = 0.005 * tiempo_marcha
        precio_acumulado_marcha.append(round(precio_marcha, ndigits=2))
        return calculate()
    while modo_taxi == 'Finalizar' or 'finalizar':
        return finish()
    return None
def finish():
    precio_final = (0.002 * sum(precio_acumulado_parado)) + (0.005 * sum(precio_acumulado_marcha))
    print(f"""
    ¡Trayecto finalizado! El precio es: {precio_final} €
    """
          )
    return restart()


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