"""
3. (2 ptos) Crear un decorador conteo.
Reglas:
- El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente.

- Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada.

- La función que vas a crear va a capturar, la edad, nombre de un alumnos y la
hora y el minuto en que fue registrado (usar la librería correspondiente de
tiempo)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”

- La función que será decorada también estará pasando 4 notas que calculará
la media del estudiante.
"""

import datetime

def conteo(funcion):

    def envoltura(*args,**kwargs):

        cant_parametros = len(args)

        if cant_parametros > 1:
            print("La función fue llamada con {} parámetros.".format(cant_parametros))

            resultado = funcion(*args)

            print("La función fue ejecutada.")
            return resultado
        else:
            print("necesita más de un parámetro para procesar la lógica.")
            return None

    return envoltura

@conteo
def registrar_estudiante(nombre, edad, nota1, nota2, nota3, nota4):

    ahora = datetime.datetime.now()
    hora = ahora.hour
    minuto = ahora.minute

    media = (nota1 + nota2 + nota3 + nota4) / 4

#mensaje
    print("{} de {} años ha sido registrado a las {} horas con {} minutos.".format(nombre,edad,hora,minuto))
    print("La media del estudiante es: {:.2f}".format(media))

    return media

# Ej1
print("correcto")
registrar_estudiante("Juana", 30, 15, 18, 12, 16)

# Ej2
print("\nmalo")
registrar_estudiante("Yami")