"""
3.Usando el concepto de funciones (3 ptos):
Reglas:
- Se requiere verificar una lista de números de diferentes países, el
área de soporte al cliente recibe diariamente ciento de números en
distintos formatos. Estos números pueden venir con o sin código,
espacios, guines, paréntesis, o hasta textos no válido

- Crear la función de normalizar_telefonos(numeros, pais_defecto) la
cual para sus parámetros tendrá las siguientes especificaciones:
numeros: lista con números telefónicos
pais_defecto: en caso no tenga un número un prefijo lo agrega de
acuerdo al país ( “PE”->”+51”, “AR”->”+54”, “CL”->”+56”)
Si el prefijo no existe entre los ya mencionados indicar un mensaje
que no es válido y que debe ingresar un prefijo válido

- Devolverá un dict con:
“válidos”: una lista de números con formato: +<código><numeroNacional>
“invalidos”: lista con los números o valores inválidos y al inicio de esa
lista agregar el valor de “NO VÁLIDOS”
- No mutará la lista de entrada original
"""


def normalizar_telefonos(numeros, pais_defecto):
    prefijos = {
    "PE": "+51",
    "AR": "+54",
    "CL": "+56"
    }

    if pais_defecto not in prefijos:
        print("El país '{}' no es compatible.".format(pais_defecto))
        return {"validos": [], "invalidos": ["NO VÁLIDOS"]}

    validos = []
    invalidos = ["NO VÁLIDOS"]
    prefijo_a_usar = prefijos[pais_defecto]

    for numero in numeros:
        # Limpiar el número de caracteres no numéricos
        numero_limpio = ""
        for numerito in numero:
            if numerito.isdigit():
                numero_limpio += numerito

        # Verificar si ya tiene un prefijo de los países soportados
        prefijo_valido = False
        for prefijo in prefijos.values():
            if numero_limpio.startswith(prefijo.replace('+', '')):
                prefijo_valido = True
                break

        if prefijo_valido:
            validos.append("+" + numero_limpio)

        elif len(numero_limpio) > 0:
            validos.append(prefijo_a_usar + numero_limpio)
        else:
            invalidos.append(numero)

    return {"validos": validos, "invalidos": invalidos}



lista_inicial = [
    "987-654-321",
   "+569876--------54521",
    "+589876--------54521",
    "(+54)123456789",
    "invalid_text",
    "987 654    321",
    "+51917855678",
]

pais_defecto = "AR"
resultado_final = normalizar_telefonos(lista_inicial, pais_defecto)


print("Lista inicial es:{} ".format(lista_inicial))

#print validaciones de numero limpio completa con el pais por defecto
print("País por defecto: {}".format(pais_defecto))
print("Números Válidos:", resultado_final["validos"])
print("Números Inválidos:", resultado_final["invalidos"])