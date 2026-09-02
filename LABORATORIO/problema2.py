class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        self.__d = float(d)
        self.__e = float(e)
        self.__f = float(f)
    def tieneSolucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0
    def getX(self):
        denominador = self.__a * self.__d - self.__b * self.__c
        if denominador == 0:
            return None
        return (self.__e * self.__d - self.__b * self.__f) / denominador
    def getY(self):
        denominador = self.__a * self.__d - self.__b * self.__c
        if denominador == 0:
            return None
        return (self.__a * self.__f - self.__e * self.__c) / denominador
if __name__ == "__main__":
    datos = input("Ingrese a, b, c, d, e, f: ").split()
    a, b, c, d, e, f = map(float, datos)
    eq = EcuacionLineal(a, b, c, d, e, f)
    if eq.tieneSolucion():
        print(f"x = {eq.getX()}, y = {eq.getY()}")
    else:
        print("La ecuación no tiene solución")