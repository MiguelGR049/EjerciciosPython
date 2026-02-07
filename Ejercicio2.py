asistencias = [
    ("Matemáticas", "Juan", "2024-09-01"),
    ("Matemáticas", "Ana", "2024-09-01"),
    ("Física", "Juan", "2024-09-01"),
    ("Matemáticas", "Juan", "2024-09-02"),
    ("Física", "Ana", "2024-09-02"),
]

# Crear un diccionario donde cada asignatura tenga un conjunto de alumnos que asistieron
def asignatura(asistencias):
    asignaturas = {}
    for asignatura, alumno, fecha in asistencias:
        if asignatura not in asignaturas:
            asignaturas[asignatura] = set()
        asignaturas[asignatura].add(alumno)
    return asignaturas
# Calcular cuántos días distintos asistío cada alumno
def diasAsistencia(asistencias):
    asistencia_alumnos = {}
    for asignatura, alumno, fecha in asistencias:
        if alumno not in asistencia_alumnos:
            asistencia_alumnos[alumno] = set()
        asistencia_alumnos[alumno].add(fecha)
    return {alumno: len(fechas) for alumno, fechas in asistencia_alumnos.items()}
# Identificar al alumno con mayor numero de asistencias totales
def mayorAsistencia(asistencias):
    asistencia_alumnos = {}
    for asignatura, alumno, fecha in asistencias:
        if alumno not in asistencia_alumnos:
            asistencia_alumnos[alumno] = 0
        asistencia_alumnos[alumno] += 1
    alumno_mayor = max(asistencia_alumnos, key=asistencia_alumnos.get)
    return alumno_mayor, asistencia_alumnos[alumno_mayor]

print(f"Alumnos que asistieron a Matemáticas: {asignatura(asistencias)['Matemáticas']}")
print(f"Alumnos que asistieron a Física: {asignatura(asistencias)['Física']}")
print(" ")
print(f"Días distintos de asistencia de Juan: {diasAsistencia(asistencias)['Juan']}")
print(f"Días distintos de asistencia de Ana: {diasAsistencia(asistencias)['Ana']}")
print(" ")
print(f"El alumno con mayor número de asistencias totales es: {mayorAsistencia(asistencias)[0]}")
