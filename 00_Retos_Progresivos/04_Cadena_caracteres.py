"""/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */"""

my_string = "Hola "
my_string02 = "Phyton"
my_string03 = "Hola mi nombre es esteban"
#Longitud 
print(len(my_string))

#Concatenación 
print(my_string + " " + my_string02 + "!")

#Repetición 
print(my_string * 4)

#Indexación
print(my_string[0])

#Slices (Rebanadas)
print(my_string02[2:6])  #[inicio:final] -> se ejecuta un valor antes del final (-1)
print(my_string02[1:]) #no colocar final es igual a ejecutar hasta el ultimo caracter o valor
print(my_string02[:5]) #No colocar inicio es igual a ejecutar el valor desde el primer caracter o valor

#Busqueda
print("P" in my_string02)
print("K" in my_string02)

#Remplazo
print(my_string.replace("a", "o")) #("Valor de la lista", "Valor por el que se cambiara")

# División
print(my_string03.split(" ")) #Corta la cadena de texto respecto al valor entregado (en este caso los espacios)