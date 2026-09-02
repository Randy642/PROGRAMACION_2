import math

class Estadistica:
    def __init__(self, datos):
        self.__datos = [float(x) for x in datos]

    def promedio(self):
        return sum(self.__datos) / len(self.__datos)

    def desviacion(self):
        prom = self.promedio()
        n = len(self.__datos)
        suma_cuadrados = sum((x - prom) ** 2 for x in self.__datos)
        return math.sqrt(suma_cuadrados / (n - 1))

# Programa de Prueba (POO)
if __name__ == "__main__":
    entrada = input("Ingrese 10 números: ").split()
    est = Estadistica(entrada)

    print(f"El promedio es {est.promedio():.2f}")
    print(f"La desviación estándar es {est.desviacion():.5f}")