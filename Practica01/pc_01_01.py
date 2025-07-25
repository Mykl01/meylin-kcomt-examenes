"""
1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (4 ptos)
Reglas:
- Asignar en variables los datos de tu nombre, salario, edad y compañía para un
usuario e identificar sus tipos de variables
- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una
conversión de datos
- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted
tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
tiene un bono del 5% en el mes diciembre”
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su
salario, según corresponda.
"""
nombre = "Meylin Kcomt"
salario = 5000.00
edad = "40"
compania = "CANTV"
edad_int = int(edad)

print ("El tipo de variable de {} que corresponde a mi nombre es : {}".format(nombre,type(nombre)))
print ("El tipo de variable de {} que corresponde a mi salario es : {}".format(salario,type(salario)))
print ("El tipo de variable de {} que corresponde a mi edad es : {}".format(edad,type(edad)))
print ("El tipo de variable de {} que corresponde a mi compania es : {}".format(compania,type(compania)))

por_bono = 0

if edad_int > 30:
    por_bono = 0.10
    print("Usted tiene un bono del 10% en el mes de diciembre")
else:
    por_bono = 0.05
    print("Usted tiene un bono del 5% en el mes de diciembre")


bono_final = pow(salario,2) + (salario*por_bono)
print ("El bono final es {}".format(bono_final))