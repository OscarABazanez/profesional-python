import time
from typing import AsyncIterable

def fibo_gen(maximo):
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            counter += 1
            aux = n1 + n2
            # Swapping 
            n1, n2 = n2, aux
            
            if maximo <= aux:
                break

            yield aux

if __name__ == "__main__":
    maximo = int( input('Ingresa el maximo valor para el fibonacci: '))
    fibonacci = fibo_gen(maximo)
    for i in fibonacci:
        print(i)
        # time.sleep(1)