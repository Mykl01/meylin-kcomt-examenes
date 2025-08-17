"""
(2 ptos) Crear un programa usando decoradores para mostrar solo la hora
y el minuto del momento que se usa el decorador
"""

def funcionhora(funcion):
    def funcionC():
        resultado = funcion()
        print("Hora después de usar la función")
        return resultado
    return funcionC

#defino las variables
hora = 10
minuto = 45

@funcionhora
def mostrar_hora():
    print("La hora es: {}:{}".format(hora, minuto))

#valida
mostrar_hora()
