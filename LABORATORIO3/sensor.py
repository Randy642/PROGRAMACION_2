class Sensor:
    tipo: str = "Genérico"
    def __init__(self, id_sensor: str):
        self.id: str = id_sensor 
        self.encendido: bool = False 
    def activar(self):
        self.encendido = True 
        print(f"Sensor {self.id} ({self.tipo}) activado.")
    def desactivar(self):
        self.encendido = False 
        print(f"Sensor {self.id} ({self.tipo}) desactivado.")
class Camara(Sensor):
    tipo: str = "Cámara" 
    def __init__(self, id_sensor: str, resolucion: str):
        Sensor.__init__(self, id_sensor) 
        self.resolucion: str = resolucion 
class SensorLuzLaser(Sensor):
    tipo: str = "Luz Laser" 
    def __init__(self, id_sensor: str, alcance: int):
        Sensor.__init__(self, id_sensor)
        self.alcance: int = alcance
class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo: str = "Vehículo Autónomo"
    def __init__(self, id_sensor: str, resolucion: str, alcance: int):
        Camara.__init__(self, id_sensor, resolucion)
        SensorLuzLaser.__init__(self, id_sensor, alcance)
    def mostrar_detalles(self):
        print(f"--- Datos del {self.tipo} ---")
        print(f"ID del dispositivo: {self.id}")
        print(f"Resolución de cámara: {self.resolucion}")
        print(f"Alcance de luz láser: {self.alcance}m")
        print(f"Estado de encendido: {self.encendido}")
if __name__ == "__main__":
    mi_vehiculo = VehiculoAutonomo(id_sensor="S-AUT-01", resolucion="1080p", alcance=50)
    mi_vehiculo.activar()
    print()
    mi_vehiculo.mostrar_detalles()
    print()
    mi_vehiculo.desactivar()