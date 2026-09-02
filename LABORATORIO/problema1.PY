import time
import random

class Cronometro:
    def __init__(self):
        self.__inicia = time.time()
        self.__finaliza = self.__inicia
    def get_inicia(self):
        return self.__inicia
    def get_finaliza(self):
        return self.__finaliza
    def inicia(self):
        self.__inicia = time.time()
    def detener(self):
        self.__finaliza = time.time()
    def lapsoDeTiempo(self):
        return (self.__finaliza - self.__inicia) * 1000
def ordenacion_por_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
if __name__ == "__main__":
    print("Generando 100,000 números aleatorios...")
    numeros = [random.randint(1, 1000) for _ in range(1000)]  
    cronometro = Cronometro()
    cronometro.inicia()   
    print("Ordenando lista mediante Selección...")
    ordenacion_por_seleccion(numeros)  
    cronometro.detener()
    print(f"Tiempo de ejecución: {cronometro.lapsoDeTiempo():.2f} ms")