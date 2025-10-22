"""/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */"""
#Listas
my_list = ["Esteban", "Laura", "Morales", "Castro"]
print(my_list)

my_list.append("Aegan") # Incersión 
print(my_list)

my_list.remove("Morales") # Elimincación 
print(my_list)

my_list[1] = "Elizabet" # Actualización 
print(my_list)

my_list.sort() # Ordenación 
print(my_list)

#Tuplas
my_tuple: tuple = ("Brais", "36", "Hijo", "Mono", "#")
print(my_tuple[1]) # Acesso

my_tuple = tuple(sorted(my_tuple)) # Ordenación (sorted entrega una lista, por ende se vuelve a colocar el constructor tuple) 

# Sets  (Estructura desordenada, no sirve para la busqueda de datos, perfecto para estructura sin duplicados)
my_set = {"Brais", "36", "Hijo", "Mono", "#"}
my_set.add("estebanmorales025") #inserción sin duplicados 
my_set.add("estebanmorales025") 
print(my_set)
my_set.remove("Brais") #Eliminación 
print(my_set)

#Dicts


#Dificultad extra
print("------------Agenda telefonica------------")
print("1) Busqueda de contactos")
print("2) Inserción de datos")
print("3) Actualización de datos")
print("4) Eliminación de datos")
