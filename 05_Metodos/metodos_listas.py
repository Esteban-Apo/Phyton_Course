frutas = ["Manzana", "Kiwi", "Manzana verde", "Papaya", "Banano"]
numeros_y_booleanos = [1,2,5,32,55,1,3243, True, 3,43, False]

#Agrega un elemento al final de la lista
frutas.append("Pitaya")
print(frutas)

#Agrega varios elementos a la lista
frutas.extend(["Laurel", "Naraja"])
print(frutas)

#Inserta un valor en indice en especifico 
frutas.insert(4, "Fresa")
print(frutas)



#Copia el valor de otro indice 
frutas[1] = frutas[4]
print(frutas)

#Organiza alfabeticamente los valores de una lista, el metodo tiene en cuenta las mayusculas iniciales y no soporta numeros.
frutas.sort()
print(frutas)

#Longitud de la lista
print("la longitud de la lista es: ", len(frutas))

#Retorna el indice de un valor dado 
indice = frutas.index("Fresa")
print(indice)

#Organiza una lista de forma ascendente (numeros y booleanos)
numeros_y_booleanos.sort()
print(numeros_y_booleanos)

#Con reverse= treu organiza los valores de forma invertida
numeros_y_booleanos.sort(reverse=True)
print(numeros_y_booleanos)

#Elimita en base al contenido de la lista
frutas.remove("Manzana")
print(frutas)


#Elimina en base al indice de la lista
frutas.pop(0)
print(frutas)

#Elimina todos los elementos
frutas.clear()
print(frutas)

