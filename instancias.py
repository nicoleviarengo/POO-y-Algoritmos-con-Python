class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return(x_diff + y_diff)**0.5

if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4,8)
#"coord_1" hace uso de la primer instancia, mientras que coord_2 al estar dentro del metodo distancia, ocupa el lugar de otra_coordenada.
    #print(coord_1.distancia(coord_2)) #A la primera cood le pasamos como parametro la coord 2
    print(isinstance(coord_2, Coordenada))