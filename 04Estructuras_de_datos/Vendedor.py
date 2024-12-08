# Ejercicio 1

##Crea la clase Vendedor con los siguientes atributos: 

# nombre: es el nombre del vendedor o vendedora.

##- anoNacemento: es el año en el que nació. No puede ser posterior a 2004. Debe ser positivo. 

##- mesNacemento: es el mes en el que nació. Debe ser un mes válido. 

##- diaNacemento: es el día en el que nació. No puede ser posterior al día 16 si el año es 2004. Debe ser un día válido segundo el mes. 

##- ventas: es el valor total en € de las ventas del vendedor o vendedora. El valor por defecto será 0. 

##- comision: es la comisión total que se lleva el vendedor o vendedora por sus ventas. El valor dependerá de las ventas, siendo siempre un 10% de las mismas pero nunca sobrepasando los 10 000€. 

#La clase dispondrá de un constructor:

#- Constructor con todos los parámetros, los que no se faciliten tomarán sus valores por defecto.

##La clase dispondrá de los siguientes métodos:

##- Setters para los atributos que tengan restricciones. 

##- setter de ventas: establecerá los nuevos valores, cumpliendo los requisitos de los atributos, es decir, modificando la comisión. 

##- metodo property de fecha de nacimiento: devolverá un String con este formato “dd/mm/aaaa”. Toda vez que se ejecutará el 16/12/2022. 

class Vendedor:
    def __init__(self, nombre, anoNacemento, mesNacemento, diaNacemento, ventas, comision):
        self.nombre = nombre
        self.anoNacemento = anoNacemento
        self.mesNacemento = mesNacemento
        self.diaNacemento = diaNacemento
        self.ventas = ventas
        self.comision = comision

    def __str__(self):
        return f"Vendedor {self.nombre} nace el {self.anoNacemento}/{self.mesNacemento}/{self.diaNacemento} con {self.ventas} € de ventas y comisión de {self.comision} €."

    def __repr__(self):
        return f"Vendedor('{self.nombre}', {self.anoNacemento}, {self.mesNacemento}, {self.diaNacemento}, {self.ventas}, {self.comision})"

    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.anoNacemento == otro.anoNacemento and self.mesNacemento == otro.mesNacemento and self.diaNacemento == otro.diaNacemento and self.ventas == otro.ventas and self.comision == otro.comision

    def __ne__(self, otro):
        return not self.__eq__(otro)

    @property
    def fechaNacimiento(self):
        return f"{self.diaNacemento}/{self.mesNacemento}/{self.anoNacemento}"

    @fechaNacimiento.setter
    def fechaNacimiento(self, fecha):
        self.diaNacemento, self.mesNacemento, self.anoNacemento = fecha.split("/")

    @property
    def ventasTotales(self):
        return self.ventas

    @ventasTotales.setter
    def ventasTotales(self, ventas):
        self.ventas = ventas
        self.comision = self.ventas * 0.1


# Prueba el funcionamiento de la clase `Libro` desde el programa principal.

vendedor = Vendedor("Juan García López", 1998, 10, 10, 10000, 100)
print(vendedor)
print(vendedor.fechaNacimiento)
print(vendedor.ventasTotales)
vendedor.ventasTotales = 20000      # Cambia el valor de ventas
print(vendedor.ventasTotales)
print(vendedor.comision)            # Imprime el valor de la comisión   de la clase `Libro` desde el programa principal.