#Listas ---------------
lista = ["Esteban", 12, True, 1.82] #Un Array puede tener una lista de elementos de diferentes tipos 
print(lista)
print(lista[0]) #forma de llamar un valor de una lista

lista[2] = 15 #El valor de una lista se puede cambiar en cualquier momento, incluso por otro tipo de dato 
print(lista[2])

#Tuplas ------------------
tupla = ("Laura", 30, False, True)
print(tupla)

#tupla[2] = 40  //No es posible cambiar el valor de una tupla despues de averla definido

#Conjunto ---------------
#El orden de los indices es totalmente modificable, no permite modificar valores
conjunto = {"Hola", "Laura Isabel Castro Muñoz", 11, True} 
conjunto = {"Valor cambiable"} #Una tupla puede cambiar su cantidad de indices, valores y tipos de datos
#print(conjunto[1]) //No es posible llamar a un conjunto por su indice


#Diccionario ----------
diccionario = {
    'Nombre' : 'Isabel',
    'Apellido' : 'Morales',
    'Edad' : 19
}

print(diccionario['Nombre']) #Es como un indice pero definiendo los valores con palabras