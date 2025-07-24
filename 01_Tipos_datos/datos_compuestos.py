#Listas ---------------
#Colección ordenada y modificable (mutable), se puede agregar, quitar o cambiar elementos
lista = ["Esteban", 12, True, 1.82] #Una Lista Puede tener elementos de diferente tipo 
print(lista)
print(lista[0]) #forma de llamar un valor especifico de una lista

lista[2] = 15 #El valor de una lista se puede cambiar en cualquier momento, incluso por otro tipo de dato 
print(lista[2])


#Tuplas ------------------
#Colección ordenada pero inmodificable(inmutable) no se pueden agregar, quitar o cambiar los elementos después de crear la tupla
tupla = ("Laura", 30, False, True)
print(tupla)
#tupla[2] = 40  //No es posible cambiar el valor de una tupla despues de averla definido


#Conjuntos ---------------
#Un conjunto es una colección no ordenada de elementos, el cual no puede tener duplicados y es modificable
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