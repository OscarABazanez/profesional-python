def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje('Oscar'))

from datetime import date, datetime


# Calcular el tiempo que se tarda en ejecutar una funcion
def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Pasaron ' + str(time_elapsed.total_seconds()) + ' segundos')
    return wrapper


@execution_time
def random_func():
    for _ in range(1,100000110):
        pass

@execution_time
def suma(a:int, b: int) -> int:
    return a + b
print('------Suma------')
suma(5,5)
print('------Ciclo------')
random_func()
