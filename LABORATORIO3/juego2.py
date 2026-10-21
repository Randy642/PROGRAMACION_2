import random
class Juego:
    def __init__(self, vidas_iniciales: int):
        self.numeroDeVidas = vidas_iniciales
        self.record = 0
    def reiniciaPartida(self):
        self.numeroDeVidas = 3
    def actualizaRecord(self):
        self.record += 1
        print(f"Récord actualizado: {self.record}")
    def quitaVida(self) -> bool:
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas: int):
        super().__init__(vidas)
        self.numeroADivinar = 0
    def validaNumero(self, numero: int) -> bool:
        """Devuelve true si el número está entre 0 y 10, en otro caso retornará false."""
        if 0 <= numero <= 10:
            return True
        return False 
    def juega(self):
        self.reiniciaPartida()
        self.numeroADivinar = random.randint(0, 10)
        while True:
            try:
                numero_ingresado = int(input("Ingresa un número (0 al 10): "))
            except ValueError:
                print("Por favor, ingresa un número entero válido.")
                continue
            if not self.validaNumero(numero_ingresado):
                continue
            if numero_ingresado == self.numeroADivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if numero_ingresado < self.numeroADivinar:
                        print("El número a adivinar es mayor.")
                    else:
                        print("El número a adivinar es menor.")
                else:
                    print(f"¡Juego terminado! Te quedaste sin vidas. El número era: {self.numeroADivinar}")
                    break
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def __init__(self, vidas: int):
        super().__init__(vidas) 
    def validaNumero(self, numero: int) -> bool:
        if super().validaNumero(numero):
            if numero % 2 == 0:
                return True
            else:
                print("Error: El número ingresado es impar. Se requiere un número par.")
                return False
        print("Error: El número debe estar entre 0 y 10.")
        return False
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self, vidas: int):
        super().__init__(vidas)
    def validaNumero(self, numero: int) -> bool:
        if super().validaNumero(numero):
            if numero % 2 != 0:
                return True
            else:
                print("Error: El número ingresado es par. Se requiere un número impar.")
                return False
        print("Error: El número debe estar entre 0 y 10.")
        return False
if __name__ == "__main__":
    print("--- 1. Juego Adivina Número ---")
    juego_normal = JuegoAdivinaNumero(3)
    juego_normal.juega()
    print("\n--- 2. Juego Adivina Número Par ---")
    juego_par = JuegoAdivinaPar(3)
    juego_par.juega()
    print("\n--- 3. Juego Adivina Número Impar ---")
    juego_impar = JuegoAdivinaImpar(3)
    juego_impar.juega()