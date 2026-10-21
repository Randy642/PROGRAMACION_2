import random
class Juego:
    def __init__(self, vidas_iniciales: int):
        self.numeroDeVidas = vidas_iniciales 
        self.record = 0 
    def reiniciaPartida(self):
        """Reinicia las vidas de la partida."""
        self.numeroDeVidas = 3 
    def actualizaRecord(self):
        """Actualiza el récord del juego."""
        self.record += 1
        print(f"¡Récord actualizado! Puntuación de récord: {self.record}") 
    def quitaVida(self) -> bool:
        """Resta una vida y retorna True si aún quedan vidas, False en caso contrario."""
        self.numeroDeVidas -= 1 
        return self.numeroDeVidas > 0   
class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas: int):
        super().__init__(vidas)
        self.numeroADivinar = 0 
    def juega(self):
        self.reiniciaPartida()
        self.numeroADivinar = random.randint(0, 10)
        while True:
            try:
                numero_ingresado = int(input("Adivina un número entre el 0 y el 10: "))
            except ValueError:
                print("Por favor, introduce un número entero válido.")
                continue
            if numero_ingresado == self.numeroADivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                quedan_vidas = self.quitaVida()
                if quedan_vidas:
                    if numero_ingresado < self.numeroADivinar:
                        print("El número a adivinar es mayor. ¡Inténtalo de nuevo!")
                    else:
                        print("El número a adivinar es menor. ¡Inténtalo de nuevo!")
                else:
                    print(f"Te has quedado sin vidas. El número secreto era: {self.numeroADivinar}")
                    break
if __name__ == "__main__":
    juego_app = JuegoAdivinaNumero(3)
    juego_app.juega()