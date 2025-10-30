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

#Ejemplos de uso de Funciones
def leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    else:
        return True
    
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = leap_year(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")



