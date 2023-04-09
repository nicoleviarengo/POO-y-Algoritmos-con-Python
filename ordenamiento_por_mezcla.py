import random

def ordenamiento_por_mezcla(lista): #Recursivoy con iterasiones
    if len(lista) > 1:
        medio = len(lista) // 2
        izq = lista[:medio] #notacion de rebanadas (:)
        der = lista[medio:]
        print(izq, '*' * 5, der)

        #llamada recursiva en cada mitas
        ordenamiento_por_mezcla(izq)
        ordenamiento_por_mezcla(der)

        #Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        #Iterador para la lista principal
        k = 0

        while i < len(izq) and j < (der):
            if izq[i] < der[j]:
                lista[k] =  izq[i]
            else:
                lista[k] = der[j]
                j+=1

            k += 1 #Para que el while no se valla al infinito

        while i < len(izq):
            lista[k] = izq[i]
            i += 1
            k += 1

        while j< len(der):
            lista[k] = der[j]
            j += 1
            k += 1

        print(f'izquierda {izq}, derecha {der}')
        print(lista)
        print('-' * 5)

    return lista 

if __name__ == '__main__':
    tamanio_de_la_lista = int(input('De que tamaño sera la lista? : '))
    
    lista = [random.randint(0, 100) for i in range(tamanio_de_la_lista)]
    print(lista)
    print('-' * 2) 

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)