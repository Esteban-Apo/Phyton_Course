#Rama Try - Except
def exeptions():
    try:
        value = int(input('Ingresa un número natural: '))
        print('El recíproco de', value, 'es', 1/value)        
    except:
        print('No se ingreso un numero natural', value)

#Realizar dos exepciones despues de un Try
def two_exeptions(): 
    try: 
        value = int(input('Ingrese un número natural: '))
        print('El recíproco de ', value, 'es', 1/value)
    except ValueError: 
        print('No se que hacer con', value)
    except ZeroDivisionError:
        print("La división entre cero no está permitida en nuestro Universo")
    
def default_exeption():
    try: 
        value = int(input('Ingrese un número natural: '))
        print('El recíproco de ', value, 'es', 1/value)
    except ValueError: 
        print('No se que hacer con', value)
    except ZeroDivisionError:
        print("La división entre cero no está permitida en nuestro Universo")
    except:
        print('Ha sucedido algo extraño, ¡Lo siento!')