
from abc import ABC, abstractmethod
from datetime import date


# ---------------- Herencia: Persona (abstracta) <- Estudiante, Docente
class Persona(ABC):
    def __init__(self, nombre, ci):
        self._nombre = nombre
        self._ci = ci

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
        self._inscripciones = []          # Asociación

    @property
    def codigo(self):
        return self._codigo

    def inscribirse(self, materia):
        insc = Inscripcion(self, materia, date.today())
        self._inscripciones.append(insc)
        materia.registrar_inscripcion(insc)
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
        self._materias = []               # Asociación

    def dictar(self, materia):
        self._materias.append(materia)
        materia.set_docente(self)

    # Dependencia: Acta se crea y se devuelve, NO se guarda como atributo
    def generar_acta(self, materia):
        return Acta(materia)

    @property
    def materias(self):
        return tuple(self._materias)

    def __str__(self):
        return f"Docente {self.nombre} ({self._especialidad})"


# ---------------- Composición: Universidad -> Carrera
class Universidad:
    def __init__(self, nombre):
        self._nombre = nombre
        self._carreras = []

    def crear_carrera(self, nombre_carrera):
        c = Carrera(nombre_carrera)       # la Universidad CREA la parte
        self._carreras.append(c)
        return c

    @property
    def nombre(self):
        return self._nombre

    @property
    def carreras(self):
        return tuple(self._carreras)


# ---------------- Agregación: Carrera -> Docente
class Carrera:
    def __init__(self, nombre):
        self._nombre = nombre
        self._docentes = []

    def agregar_docente(self, docente):   # AGREGA partes ya existentes
        self._docentes.append(docente)

    @property
    def nombre(self):
        return self._nombre

    @property
    def docentes(self):
        return tuple(self._docentes)


# ---------------- Composición: Materia -> Horario
class Materia:
    def __init__(self, codigo, creditos):
        self._codigo = codigo
        self._creditos = creditos
        self._docente = None
        self._horarios = []
        self._inscripciones = []

    def agregar_horario(self, fecha, aula):
        h = Horario(fecha, aula)
        self._horarios.append(h)
        return h

    def registrar_inscripcion(self, inscripcion):
        self._inscripciones.append(inscripcion)

    def set_docente(self, docente):
        self._docente = docente

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
    def __init__(self, fecha, aula):
        self._fecha = fecha
        self._aula = aula

    @property
    def fecha(self):
        return self._fecha

    @property
    def aula(self):
        return self._aula


# ---------------- Interfaz Calificable (ABC) e Inscripcion
class Calificable(ABC):
    @abstractmethod
    def calcular_nota(self):
        ...


class Inscripcion(Calificable):
    def __init__(self, estudiante, materia, fecha):
        self._estudiante = estudiante
        self._materia = materia
        self._fecha = fecha
        self._nota = 0.0

    def registrar_nota(self, nota):
        if nota < 0 or nota > 100:
            raise ValueError("La nota debe estar entre 0 y 100")
        self._nota = float(nota)

    def calcular_nota(self):
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


# ---------------- Dependencia: Docente usa Acta
class Acta:
    def __init__(self, materia):
        self._fecha = date.today()
        lineas = [f"ACTA {materia.codigo} - {self._fecha}"]
        for i in materia.inscripciones:
            lineas.append(f"  {i.estudiante.nombre}: {i.calcular_nota()}")
        self._contenido = "\n".join(lineas)

    def __str__(self):
        return self._contenido


# =====================================================================
def punto_1():
    print("=" * 60, "\nPUNTO 1 - Ejecución del código base\n" + "=" * 60)
    umsa = Universidad("UMSA")
    informatica = umsa.crear_carrera("Informática")

    docente = Docente("Ana Alba", "1234567", "Ingeniería de Software")
    informatica.agregar_docente(docente)

    poo = Materia("INF-121", 6)
    docente.dictar(poo)

    poo.agregar_horario(date(2026, 7, 2), "Aula 101")
    poo.agregar_horario(date(2026, 7, 9), "Aula 101")

    e1 = Estudiante("Carlos Flores", "7654321", "E-001")
    e2 = Estudiante("Maria Salas", "7654322", "E-002")
    i1 = e1.inscribirse(poo)
    i2 = e2.inscribirse(poo)
    i1.registrar_nota(85)
    i2.registrar_nota(92)

    # Herencia + polimorfismo
    for p in [docente, e1, e2]:
        print(p)

    c: Calificable = i1
    print(f"Nota de {e1.nombre}: {c.calcular_nota()}")

    print(docente.generar_acta(poo))


def punto_6_problemas():
    print("\n" + "=" * 60, "\nPUNTO 6 - Casos inconsistentes en el código BASE\n" + "=" * 60)

    # Caso 1: doble inscripción
    poo = Materia("INF-121", 6)
    e1 = Estudiante("Carlos Flores", "7654321", "E-001")
    e1.inscribirse(poo)
    e1.inscribirse(poo)
    d = Docente("Ana Alba", "1234567", "Software")
    d.dictar(poo)
    print("\n[Doble inscripción] El acta imprime dos veces al estudiante:")
    print(d.generar_acta(poo))

    # Caso 2: dos docentes en un curso
    m = Materia("INF-122", 6)
    d1 = Docente("Docente 1", "1", "A")
    d2 = Docente("Docente 2", "2", "B")
    d1.dictar(m)
    d2.dictar(m)
    print("[Dos docentes] materia.docente =", m.docente.nombre,
          "| pero d1 sigue creyendo que dicta:", len(d1.materias), "materia(s)")

    # Caso 3: nota sin registrar
    m3 = Materia("INF-123", 5)
    e3 = Estudiante("Luis", "3", "E-003")
    i3 = e3.inscribirse(m3)
    print("[Nota sin registrar] calcular_nota() =", i3.calcular_nota(),
          "(indistinguible de un 0 real)")

    # Caso 4: docente en dos carreras
    u = Universidad("UMSA")
    c1, c2 = u.crear_carrera("Informática"), u.crear_carrera("Estadística")
    c1.agregar_docente(d1)
    c2.agregar_docente(d1)
    print("[Docente en dos carreras] d1 está en",
          [c.nombre for c in (c1, c2) if d1 in c.docentes])

    # Caso 5: composición no estricta
    h_suelto = Horario(date(2026, 7, 2), "Aula 999")   # equivale a new Sesion(...)
    m.agregar_horario(date(2026, 7, 9), "Aula 1")
    m._horarios.append(h_suelto)                        # (y puede compartirse entre materias)
    print("[Composición no estricta] Horario creado fuera de Materia:", h_suelto.aula)


if __name__ == "__main__":
    punto_1()
    punto_6_problemas()