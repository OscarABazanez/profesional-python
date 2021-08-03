import time


class FiboIter():
    def __init__(self, maximo):
        self.maximo = maximo


    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self


    def  __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            # Sin swapping 
            # self.n1 = self.n2
            # self.n2 = self.aux

            # Con swapping 
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
        
        if self.aux >= self.maximo:
            raise StopIteration

        return self.aux

if __name__ == "__main__":
    maximo = int(input('Ingresa el maximo valor para el fibonacci: '))
    fibonacci = FiboIter(maximo)
    for element in fibonacci:
        print(element)
        if maximo <= 100:
            time.sleep(0.5)
