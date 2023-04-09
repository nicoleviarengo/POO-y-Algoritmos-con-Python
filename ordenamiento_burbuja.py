import random 

def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n): #recorremos la lista n veces
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n*n) = O(n**2) 
                                      #n - lo que ya recorrimos - 1
            if lista[j] > lista[j + 1]: #comparamos los elementos adyacentes
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #intercambiar los elementos
    return lista

if __name__ == '__main__':
    tamanio_de_la_lista = int(input('De que tamaño sera la lista? : '))
    
    lista = [random.randint(0, 100) for i in range(tamanio_de_la_lista)]
    
    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)
   