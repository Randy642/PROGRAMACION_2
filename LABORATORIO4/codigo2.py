from abc import ABC, abstractmethod
from datetime import date
_CREADOR = object()
class Persona(ABC):
    def __init__(self, nombre, ci):
        self._nombre, self._ci = nombre, ci
    @property
    def nombre(self):
        return self._nombre
    @property
    def ci(self):
        return self._ci
    @abstractmethod
    def __str__(self):
        ...
class Estudiante(Persona):
    def __init__(self, nombre, ci, codigo):
        super().__init__(nombre, ci)
        self._codigo = codigo
        self._inscripciones = []
    @property
    def codigo(self):
        return self._codigo
    def inscribirse(self, materia):
        for i in self._inscripciones:
            if i.materia is materia:
                raise ValueError(f"{self.nombre} ya está inscrito en {materia.codigo}")
        insc = Inscripcion(self, materia, date.today())
        self._inscripciones.append(insc)
        materia._registrar_inscripcion(insc)
        return insc
    @property
    def inscripciones(self):
        return tuple(self._inscripciones)
    def __str__(self):
        return f"Estudiante {self.nombre} (código {self._codigo})"
class Docente(Persona):
    def __init__(self, nombre, ci, especialidad):
        super().__init__(nombre, ci)
        self._especialidad = especialidad
        self._materias = []
        self._carrera = None
        self._ayudantes = []
    def dictar(self, materia):
        if materia.docente is not None and materia.docente is not self:
            raise ValueError(f"{materia.codigo} ya la dicta {materia.docente.nombre}")
        if materia not in self._materias:
            self._materias.append(materia)
            materia._set_docente(self)
    def generar_acta(self, materia):     
        return Acta(materia)
    def _registrar_ayudante(self, ayudante):
        self._ayudantes.append(ayudante)
    @property
    def carrera(self):
        return self._carrera
    @property
    def materias(self):
        return tuple(self._materias)
    @property
    def ayudantes(self):
        return tuple(self._ayudantes)
    def __str__(self):
        return f"Docente {self.nombre} ({self._especialidad})"
class Ayudante(Estudiante):
    def __init__(self, nombre, ci, codigo):
        super().__init__(nombre, ci, codigo)
        self._docente = None
    def colaborar_con(self, docente):
        if self._docente is not None:
            raise ValueError(f"{self.nombre} ya colabora con {self._docente.nombre}")
        self._docente = docente
        docente._registrar_ayudante(self)
    @property
    def docente(self):
        return self._docente
    def __str__(self):
        colab = self._docente.nombre if self._docente else "nadie"
        return f"Ayudante {self.nombre} (código {self.codigo}) colabora con {colab}"
class Universidad:
    def __init__(self, nombre):
        self._nombre = nombre
        self._carreras = []
    def crear_carrera(self, nombre):
        c = Carrera(nombre, _creador=_CREADOR)
        self._carreras.append(c)
        return c
    @property
    def nombre(self):
        return self._nombre
    @property
    def carreras(self):
        return tuple(self._carreras)
class Carrera:
    def __init__(self, nombre, _creador=None):
        if _creador is not _CREADOR:
            raise TypeError("Una Carrera solo puede crearla una Universidad")
        self._nombre = nombre
        self._docentes = []
    def agregar_docente(self, docente):
        if docente.carrera is not None and docente.carrera is not self:
            raise ValueError(f"{docente.nombre} ya pertenece a {docente.carrera.nombre}")
        if docente not in self._docentes:
            self._docentes.append(docente)
            docente._carrera = self
    @property
    def nombre(self):
        return self._nombre
    @property
    def docentes(self):
        return tuple(self._docentes)
class Materia:
    def __init__(self, codigo, creditos):
        self._codigo, self._creditos = codigo, creditos
        self._docente = None
        self._horarios = []
        self._inscripciones = []
    def agregar_horario(self, fecha, aula):
        h = Horario(fecha, aula, _creador=_CREADOR)
        self._horarios.append(h)
        return h
    def _registrar_inscripcion(self, i):
        self._inscripciones.append(i)
    def _set_docente(self, d):
        self._docente = d
    @property
    def codigo(self):
        return self._codigo
    @property
    def creditos(self):
        return self._creditos
    @property
    def docente(self):
        return self._docente
    @property
    def horarios(self):
        return tuple(self._horarios)
    @property
    def inscripciones(self):
        return tuple(self._inscripciones)
class Horario:
    def __init__(self, fecha, aula, _creador=None):
        if _creador is not _CREADOR:
            raise TypeError("Un Horario solo puede crearlo una Materia")
        self._fecha, self._aula = fecha, aula
    @property
    def fecha(self):
        return self._fecha
    @property
    def aula(self):
        return self._aula
class Calificable(ABC):
    @abstractmethod
    def calcular_nota(self):
        ...
class Inscripcion(Calificable):
    def __init__(self, estudiante, materia, fecha):
        self._estudiante, self._materia, self._fecha = estudiante, materia, fecha
        self._nota = None           
    def registrar_nota(self, nota):
        if nota < 0 or nota > 100:
            raise ValueError("La nota debe estar entre 0 y 100")
        self._nota = float(nota)
    @property
    def tiene_nota(self):
        return self._nota is not None
    def calcular_nota(self):
        if self._nota is None:
            raise ValueError(f"{self._estudiante.nombre} no tiene nota registrada")
        return self._nota
    @property
    def estudiante(self):
        return self._estudiante
    @property
    def materia(self):
        return self._materia
    @property
    def fecha(self):
        return self._fecha
class Acta:
    def __init__(self, materia):
        self._fecha = date.today()
        lineas = [f"ACTA {materia.codigo} - {self._fecha}"]
        for i in materia.inscripciones:
            nota = i.calcular_nota() if i.tiene_nota else "SIN NOTA"
            lineas.append(f"  {i.estudiante.nombre}: {nota}")
        self._contenido = "\n".join(lineas)
    def __str__(self):
        return self._contenido
def intentar(titulo, accion):
    try:
        accion()
        print(f"[{titulo}] ERROR: debió fallar")
    except (ValueError, TypeError) as e:
        print(f"[{titulo}] rechazado -> {e}")
def main():
    umsa = Universidad("UMSA")
    informatica = umsa.crear_carrera("Informática")
    estadistica = umsa.crear_carrera("Estadística")
    d1 = Docente("Ana Alba", "1234567", "Ingeniería de Software")
    d2 = Docente("Pedro Rojas", "1111111", "Bases de Datos")
    informatica.agregar_docente(d1)
    poo = Materia("INF-121", 6)
    d1.dictar(poo)
    e1 = Estudiante("Carlos Flores", "7654321", "E-001")
    e2 = Estudiante("Maria Salas", "7654322", "E-002")
    e1.inscribirse(poo)
    e2.inscribirse(poo)
    print("--- Punto 6: correcciones ---")
    intentar("Doble inscripción", lambda: e1.inscribirse(poo))
    intentar("Dos docentes", lambda: d2.dictar(poo))
    intentar("Docente en dos carreras", lambda: estadistica.agregar_docente(d1))
    intentar("Horario fuera de Materia", lambda: Horario(date(2026, 7, 2), "Aula 9"))
    intentar("Carrera fuera de Universidad", lambda: Carrera("Fantasma"))
    intentar("Nota sin registrar", lambda: e1.inscripciones[0].calcular_nota())
    e1.inscripciones[0].registrar_nota(85)
    e2.inscripciones[0].registrar_nota(92)
    print("\n" + str(d1.generar_acta(poo)))
    print("\n--- Punto 7: Ayudante ---")
    a = Ayudante("Rosa Quispe", "9999999", "E-010")
    a.colaborar_con(d1)
    print(a)
    print("Es Estudiante:", isinstance(a, Estudiante), "| Ayudantes de", d1.nombre, "->",
          [x.nombre for x in d1.ayudantes])
    a.inscribirse(poo)          
    intentar("Ayudante con 2 docentes", lambda: a.colaborar_con(d2))
if __name__ == "__main__":
    main()
