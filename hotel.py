#Atributos de la instancia

class Hotel:
    def __init__(self, nummax_de_huespedes, estacionamiento):
        self.nummax_de_huespedes=nummax_de_huespedes
        self.estacionamiento=estacionamiento
        self.huespedes=0
        hotel=Hotel(nummax_de_huespedes=50, estacionamiento=20)
        print(hotel, estacionamiento)

#Metodos de instancia
    def aniadir_huspedes(self, cant_huespedes):
        self.huespedes += cant_huespedes
        

    def checkout(self, cant_huespedes):
        self.huespedes -= cant_huespedes

    def ocupacion_total(self):
        return self.huespedes
    


