#Colección ordenada y modificable (mutable), se puede agregar, quitar o cambiar elementos

frutas = ["manzana", "banana", "naranja"]
frutas.append("kiwi")         # Agrega un elemento
frutas[1] = "pera"            # Cambia "banana" por "pera"
print(frutas)                 # ['manzana', 'pera', 'naranja', 'kiwi']


#Si se asigna un valor de una lista a otra, las listas no se copiaran, 
# si no que Apuntaran a la misma lista en la memoria

vehicles_one = ['coche', 'bicicleta', 'motor']
print(vehicles_one) # output: ['coche', 'bicicleta', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0] # elimina 'coche'
print(vehicles_two) # output: ['bicicleta', 'motor']


#Si deseas copiar una lista o parte de la lista, puedes hacerlo haciendo uso de rebanadas
colors = ['rojo', 'verde', 'naranja']

copy_whole_colors = colors[:]  # copia la lista entera
copy_part_colors = colors[0:2]  # copia parte de la lista

#Eliminar rebanadas 
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # output: [3, 4, 5]

del my_list[:]
print(my_list)  # elimina el contenido de la lista, genera: []

