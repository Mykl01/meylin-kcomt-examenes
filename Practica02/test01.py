"""
Reglas:
- Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas.
- Calcular el promedio de cada estudiantes.
- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
y el valor sea otro diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor
- Mostrar en pantalla el estudiante con mayor promedio
"""


def procesar_notas(estudiantes):
    resultados = {}

    for nom_est, notas in estudiantes.items():
        prom = sum(notas) / len(notas)

        # Aprobado o no ?
        if prom >= 11:
            estado = "aprobado"
        else:
            estado = "desaprobado"

        resultados[nom_est] = {
            'promedio': prom,
            'estado': estado
        }
    return resultados

estudiantes_01 = {
    'Luis': [15, 12, 12],
    'Mario': [10, 8, 12],
    'Maria': [16, 15, 16],
    'Juana': [7, 8, 6]
}

# valida la funcion
resultados_procesados = procesar_notas(estudiantes_01)

# estudiante con mayor prom
mayor_prom = 0
est_mayor_prom = ""

for nom_est, datos in resultados_procesados.items():
    if datos['promedio'] > mayor_prom:
        mayor_prom = datos['promedio']
        est_mayor_prom = nom_est

for nom_est, datos in resultados_procesados.items():
     print("Estudiante: {}, prom: {:.2f}, Estado: {}".format(nom_est,datos['promedio'],datos['estado']))

# print salida resultado estudiante con promedio
print("El estudiante con el mayor promedio es {} con un prom de {:.2f}".format(est_mayor_prom,mayor_prom))