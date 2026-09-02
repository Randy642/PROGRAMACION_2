import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
    def getDiscriminante(self):
        return (self.__b ** 2) - (4 * self.__a * self.__c)
    def getRaiz1(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.__b + math.sqrt(disc)) / (2 * self.__a)
    def getRaiz2(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.__b - math.sqrt(disc)) / (2 * self.__a)
if __name__ == "__main__":
    datos = input("Ingrese a, b, c: ").split()
    a, b, c = map(float, datos)
    eq = EcuacionCuadratica(a, b, c)
    disc = eq.getDiscriminante()

    if disc > 0:
        print(f"La ecuación tiene dos raíces {eq.getRaiz1():.6f} y {eq.getRaiz2():.6f}")
    elif disc == 0:
        print(f"La ecuación tiene una raíz {eq.getRaiz1():.0f}")
    else:
        print("La ecuación no tiene raíces reales")