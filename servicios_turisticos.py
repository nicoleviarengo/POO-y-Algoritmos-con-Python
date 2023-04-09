#Grupo: Viarengo Nicole, Alvarez Grandolli Oriana, Farber Agustin

#definimos las clases con sus atributos
class Guia:
    def datos(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

class Servicio:
    def atributos(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

#un guia quiere ofrecer un servicio
def main():
    #verificamos el dni
    DNI = input("Ingrese su DNI: ")
    if(DNI == Guia.dni):
        print("Ya esta registrado")
    else:
    #no esta registrado, registra sus datos
        print("Registro de los datos del guia")
        Guia.nombre = input("Nombre: ")
        Guia.apellido = input("Apellido: ")
        Guia.dni = input("DNI: ")

    #el guia registra los datos del servicio a ofrecer
    Servicio.nombre = input("Nombre del servicio: ")
    Servicio.descripcion = input("Ingrese la descripcion del servicio: ")
    Servicio.precio = input("Precio del servicio: ")

if '__name__'=='__main__':
    main()