"""
2. Usando el concepto de funciones (3 ptos):
Reglas:
- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombres los debe separar (si debe haber el caso)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original
"""


def normalizar_nombres(nombres):
    nombres_normalizados = []

    for nombre in nombres:
        nombre_limpio = nombre.strip().title()
        print("Nombre Sin espacios al inicio o al final (formato titulo) '{}' -> '{}'".format(nombre,nombre_limpio))

        nombrecito = nombre_limpio.split()
        print("Nombre Separado: {}".format(nombrecito))

        for nombrecito in nombrecito:
            if nombrecito not in nombres_normalizados:
                nombres_normalizados.append(nombrecito)
    return nombres_normalizados

#valida la funcion
lista_nom = [
    "Ali cia ",
    " Li za Maria",
    "ANA MARIA",
    "   Rosa maria   ",
    " Carlos Enrique ",
    "mila gritos ",
    " Luis Enrique ",
]
#
nombres_normalizados = normalizar_nombres(lista_nom)

print("Lista Inicial:", lista_nom)
print("Lista normalizada:", nombres_normalizados)