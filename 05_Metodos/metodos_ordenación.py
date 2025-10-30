#El ordenamiento burbuja funciona comparando pares de elementos adyacentes (uno al lado del otro)
#y los intercambia  si están en el orden incorrecto (por ejemplo, si el primero es mayor que el segundo).

def bubble_sort(): #Algoritmo de ordenamiento burbuja
    my_list = [8, 10, 6, 2, 4]  # lista a ordenar
    swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

    while swapped:
        swapped = False  # no hay intercambios hasta ahora
        for i in range(len(my_list) - 1): #len(my_list) entrega la cantidad total de elementos y "-1" el Indice total de la lista
            if my_list[i] > my_list[i + 1]: #Compara el valor "i", con el elemento el elemento siguiente "i + 1"
                swapped = True  # ¡ocurrió el intercambio!
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    
    print(my_list)


def interactive_bubble_sort():
    my_list = []
    swapped = True
    num = int(input("¿Cuántos elementos deseas ordenar?: "))

    for i in range(num):
        val = float(input("Ingresa un elemento de la lista: "))
        my_list.append(val)

    while swapped:
        swapped = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                swapped = True
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    print("\nOrdenada:")
    print(my_list)

interactive_bubble_sort()