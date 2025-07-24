"""EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.s"""

#1  Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#Operadorea aricméticos 
#Suma y resta
suma = 4 + 5
resta = 6 - 3
print(suma, resta)

#Multiplicación y División 
multi = 5 * 5
div = 8 / 4
print(multi, div)

#División Baja
div_low = 12 // 5
print(div_low)

#Exponente
expo = 12**5
print(expo)

#Resto o Modulo 
resto = 12 % 5
print(resto)


#Operadores Logicos 
#AND
resultado1 = True & True #Devuelve True
resultado2 = True & False #Devuelve False
resultado3 = False & False #Devuelve False
resultado4 = False & True #Devuelve False

#OR     
resultado5 = True | True #Devuelve True
resultado6 = False | True #Devuelve True
resultado7 = True | False #Devuelve True
resultado8 = False | False #Devuelve False

#NOT
resultado9 = not True #Devuelve false (Es como decir no verdadero, entonces es falso)
resultado10 = not False #Devuelve True (no Falso, entonces verdadero )


#Operadores de comparación 
igual_que = 5 == 7

distinto_que = 5 != 7

mayor_que = 5 > 7

menor_que = 5 < 7

mayor_o_igual = 5 >= 7

menor_o_igual = 5 <= 7


#Operadores de asignación 
a = 13
b = 10
b += 13
c = "esteban"

#Operadores de identidad (Los operadores is y is not comparan las direcciones de memoria de dos objetos )
#Is
a = [1, 2, 3]
b = a

es_igual = (a is b)  # True, ya que a y b se refieren al mismo objeto

#Is not
x = 10
y = 10

no_es_igual = (x is not y)  # False, ya que x e y se refieren al mismo objeto



#Operadores de Pertenencia (verificar si un valor está presente dentro de una secuencia)
#In
frutas = ["manzana", "banana", "cereza"]

es_banana = "banana" in frutas # True
es_uva = "uva" in frutas # False

#Operador Not In
frutas2 = ["manzana", "banana", "cereza"]
no_es_uva = "uva" not in frutas # True
no_es_manzana = "manzana" not in frutas # False



#2 Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#que representen todos los tipos de estructuras de control que existan
#Condicionales, iterativas, excepciones.

#Condicionales
edad_persona1 = 18
if edad_persona1 >= 18: #Si esta condición se cumple, se ejecuta el codigo correspondiente
    print("Puedes pasar, eres mayor de edad")
elif edad_persona1 >= 6 & edad_persona1 < 18: #Si la anteriro condición no se cumple se ejecuta esta función.
    print("No puedes pasar, eres menor de edad")
else:
    print("Que edad tienes?, eres demasiado pequeño") #Si ninguna condición se cumple, se ejecuta esta condición


#Iterativas
lista_one = ["esteban", "Laura", "amor", 12]
tupla_one = ("uuu", 30, 3.5, True)
conjunto_one = {"Hola", "Laura Isabel Castro Muñoz", 11, True} 
diccionario_ejercice = {
    'Nombre' : 'Isabel',
    'Apellido' : 'Morales',
    'Edad' : 19
}

#exepciones
try:
    # Código que puede lanzar una excepción
    resultado = 10 / 2
except ZeroDivisionError:
    # Código a ejecutar si se produce una excepción del tipo ZeroDivisionError
    print("No se puede dividir por cero.")
else:
    # Código a ejecutar si no se produce ninguna excepción
    print("La división fue exitosa. El resultado es:", resultado)
finally:
    # Código a ejecutar siempre, independientemente de si se produce una excepción o no
    print("Esta línea se ejecutará siempre.")


""" DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.s"""

for i in range (10, 56): #Rango de valores entre 10 y 56
    modulo = i % 3 #Sacamos el resto 
    if modulo != 0 and i != 16: #SI el resto es cero y a su vez i es diferente de 16, se imprime el valor
        print(i)


