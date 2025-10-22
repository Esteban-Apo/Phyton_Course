#Estructura basica de una función 
def funcion_one (): 
    print("Codigo de la función")

#Funcion con parametros 
def funcion_two (number):
    print("El numero es: ", number)


funcion_one() #Forma de llamar a la función 
funcion_two(1) #Funcion con parametros 

#Paso de argumentos con palabras clave
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

