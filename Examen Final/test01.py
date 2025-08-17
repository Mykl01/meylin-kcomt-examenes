"""
Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
- Crear una clase llamada Empleado donde sus atributos deben ser
nombre, edad, sueldo y de nacionalidad peruana,
tendrá un método para solicitar su nombre
y otro para solicitar su edad.
Así como un método cumpleaños donde cada vez que invoque aumentará en un año la edad de la persona.


- Crear la instancia de la clase Empleado y usar el nuevo método
aumentoSueldo que incrementar su sueldo en un 30% (mínimo instanciar la
clase 2 veces, mostrar por pantalla dicho sueldo ya incrementado).

- Crear un siguiente método prediccion() que retorne un mensaje donde
indique que: “En el año XXXX tendrá XX años”, el año se ingresará por
parámetro y la edad también, realizar una validación si la edad ingresada por
parámetro es menor a la del constructor indicar que no es posible realizar la
operación (Mostrar por pantalla este valor)
Aplicando la definición de Herencias. Crear una clase llamada Persona
(Que heredará de la anterior Clase) y agregar un atributo sueldo a esta
clase

- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la clase Empleado que llame al método
pueda transferir la cantidad monto al objeto Empleado2 por consiguiente
deberá ir actualizando también el saldo o monto que tiene el otro empleado
en su cuenta cada vez que use el método transferencia

- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase realizando una
transferencia y con dos personas.

"""
class Empleado:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.nacionalidad = "peruana"

    def solicitar_nombre(self):
        self.nombre = input("ingresar el nombre del empleado: ")

    def solicitar_edad(self):
        self.edad = int(input("ingresar la edad del empleado: "))

    def cumpleanos(self):
        self.edad += 1
        print("Feliz cumpleaños, {} Ahora tiene {} años.".format(self.nombre,self.edad))

    def aumento_sueldo(self):
        self.sueldo *= 1.30
        print("El sueldo de {} ahora es S/.{:.2f}".format(self.nombre,self.sueldo))

    def prediccion(self, annio_prediccion, edad_param):
        if edad_param < self.edad:
            print(
                "No se puede realizar la operacion.La edad ingresada  es menor a la edad del empleado.")
            return

        annio_actual = 2025
        edad_futura = self.edad + (annio_prediccion - annio_actual)
        print("En el año {} tendra {} años.".format(annio_prediccion,edad_futura))


#validacion uso de la clase
print("validacion")
emp1 = Empleado("yami", 25, 5600)
emp2 = Empleado("Luis", 30, 3000)

emp1.aumento_sueldo()
emp2.aumento_sueldo()

print("print salida")
emp1.prediccion(2030, 25)
emp1.prediccion(2028, 20)