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

#Diccionario
my_dict: dict = {
    "name" : "esteban",
    "surname" : "Morales",
    "age" : "36"
}
print(my_dict["surname"]) # Acceso

my_dict["height"] = "1.78" # Inserción
print(my_dict)

my_dict["age"] = "37" #Actualización 

my_dict = dict(sorted(my_dict.items())) # Ordenación 
print(my_dict)
print(type(my_dict))



#Dificultad extra
def my_agend():
    agenda = {}

    while True: 

        print("\n------------Agenda telefonica------------")
        print("")
        print("1) Busqueda de contactos")
        print("2) Inserción de datos")
        print("3) Actualización de datos")
        print("4) Eliminación de datos")
        print("5) salir")
        opcion = input("\nEscoge una opción: ")

        match opcion: 
            case "1": 
                print("\n--------Busqueda de contactos--------")
                name = input("Escriba el nombre del contacto que desea buscar:  ")
                if name in agenda: 
                    print(f"El numero asociado al nombre: {name}, es: {agenda[name]}")
                else: 
                    print(f"El nombre {name} no esta en la agenda")
            case "2":
                print("\n--------Inserción de contactos--------")
                name = input("Digite el nombre del contacto: ")
                phone = input("Digite el numero del contacto: ")
                if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                    agenda[name] = phone
                else: 
                    print("Debes introducir un número de telefono de un máximo de 11 dígitos.")
            case "3":
                input("Digite el nombre que desea Actualizar: ")
                if name in agenda:
                    name = input("Digite el nombre del contacto: ")
                    phone = input("Digite el numero del contacto: ")
                    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                        agenda[name] = phone
                    else:
                        print("Debes introducir un número de telefono de un máximo de 11 dígitos.")
                else: 
                     print(f"El contacto {name} no existe.")

            case "4":
                input("Digite el nombre que desea eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:   
                    print("El nombre no se encuentra en la agenda.")
            case "5":
                print("Saliendo de la agenda....")
                break
            case _: #_ para valores diferentes a los CASE
                print("Porfavor escriba un numero referente a la lista....")


my_agend()