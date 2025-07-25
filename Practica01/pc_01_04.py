"""
- Caso: Calculadora de propinas
Crea un programa que permita ingresar el total de una cuenta en un restaurante,
el porcentaje de propina que desea dejar el cliente y el número de personas que
dividirán la cuenta.

 El programa debe mostrar:
El monto total con propina.
El monto que debe pagar cada persona (con 2 decimales).

Un mensaje será personalizado, indicará si el monto individual supera los 100
soles, mostrando un mensaje de advertencia si es el caso.

Entrada esperada (por input):
Total de la cuenta: float
Porcentaje de propina: float
Número de personas: int
Salida ejemplo (output):
Monto total con propina: S/. 230.00
Cada persona debe pagar: S/. 115.00
¡Advertencia! El monto por persona supera los S/. 100

"""


total_cuenta = float(210)
porc_propina = float (0.10)
num_personas = int (2)

monto_persona = (total_cuenta + (total_cuenta*porc_propina))/num_personas
monto_propina = total_cuenta*porc_propina
monto_total_con_propina = (total_cuenta + (total_cuenta*porc_propina))

if total_cuenta < 0 or porc_propina < 0 or num_personas < 0:
    print("Verifique los datos ingresados, existen valores no validos")
else :
    print("El monto total a pagar es S./ {:.2f}.\nEl monto total de propina es S./{} y cada persona debe pagar S./{}".format(monto_total_con_propina,monto_propina,monto_persona))

if monto_persona > 100:
    print("El monto de la cuenta por persona supera los S./ 100")
else :
    print("El monto total a pagar es S./{:.2f} ./n El monto total de propina es {} y cada persona debe pagar S./{}".format(monto_total_con_propina,monto_propina,monto_persona))

