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



def largest_value():
    my_list = [7, 3, 11, 5, 1, 9, 7, 15, 13]
    largest = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]

    print(largest)

#largest_value()

def find_number():
    my_list02 = [2, 4, 3, 5, 11, 5]
    to_find = 5
    found = False 

    for i in range (len(my_list02)):
        if to_find == my_list02[i]:
            found = True
            break
    if found:
        print(f"El numero encontrado fue:", my_list02[i], "en el indice: ", i )
    else: 
        print("Indice no encontrado")
        
#Triangulos 
def is_a_triangle(a,b,c):
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if c + b <= a:
        return False
    return True 
    

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


