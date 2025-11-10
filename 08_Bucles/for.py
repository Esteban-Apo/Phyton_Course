#Estrutura for
"""
for i in range(100):
    # do_something()
    pass
"""

def loop_for():

    for i in range(10):
        print("El valor de i es", i)

def mississippi_time():
    import time #Importar librería para casos muy concretos (uso de la librería solo en una función )

    # Escribe un bucle for que cuente hasta cinco.
        # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
        # Cuerpo del bucle, emplea : time.sleep(1)
    for i in range(1, 6):
        print(i,"Un mississippi")
        time.sleep(1)
    # Escribe una función print con el mensaje final.

    print("List0 o no, aquí vengo!")

def break_and_continue():

    # break - ejemplo
    print("La instrucción break:")
    for i in range(1, 6):
        if i == 3:
            break
        print("Dentro del bucle.", i)
    print("Fuera del bucle.")


    # continue - ejemplo
    print("\nLa instrucción continue:")
    for i in range(1, 6):
        if i == 3:
            continue
        print("Dentro del bucle.", i)
    print("Fuera del bucle.")

def numbers_not_repit():
    
    my_list03 = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
    # el Metodo Fromkeys convierte los valores en llaves, por ende tiene que ser valores unicos 
    #Lo que permite eliminar los valores duplicados
    
    my_list03 = list(dict.fromkeys(my_list03)) 
    print("La lista con elementos únicos:")
    print(my_list03)

#loop_for()
#mississippi_time()
#break_and_continue()
#numbers_not_repit()

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])

