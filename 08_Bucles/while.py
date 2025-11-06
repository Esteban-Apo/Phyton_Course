"""while conditional_expression:
    instruction_one
    instruction_two
    instruction_three
    :
    :
    instruction_n
 """
def infinit_loop ():
    #Bucle infinito 
    while True: 
        print("Estoy atrapado en un bucle")
        break #Finalizamos el bucle


def ej_one_pares_impares():
    #Ejemplos de bucle While 

    # Un programa que lee una secuencia de números
    # y cuenta cuántos números son pares y cuántos son impares.
    # El programa termina cuando se ingresa un cero.
    
    odd_numbers = 0
    even_numbers = 0
    
    # Lee el primer número.
    number = int(input("Introduce un número o escribe 0 para detener: "))
    
    # 0 termina la ejecución.
    while number != 0:
        # Verificar si el número es impar.
        if number % 2 == 1:
            # Incrementar el contador de números impares odd_numbers.
            odd_numbers += 1
        else:
            # Incrementar el contador de números pares even_numbers.
            even_numbers += 1
        # Leer el siguiente número.
        number = int(input("Introduce un número o escribe 0 para detener: "))
    
    # Imprimir resultados.
    print("Conteo de números impares:", odd_numbers)
    print("Conteo de números pares:", even_numbers)


#Ej 2

def secret_number_ej_2 ():


    secret_number = 777

    print(
    """
    +================================+
    | ¡Bienvenido a mi juego, muggle!|
    | Introduce un número entero     |
    | y adivina qué número he        |
    | elegido para ti.               |
    |¿Cuál es el número secreto?     |
    +================================+
    """)
    
    while True:
        secret_number = int(input("Adivina el numero: "))
        if secret_number == 777:
            print("Numero Correcto")
            break
        else: 
            print("Sigues en el bucle")
    
    print("Saliste del bucle")


#infinit_loop() 
#ej_one_pares_impares()
secret_number_ej_2()