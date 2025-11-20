#Uso de la serie Fibonacci para demostrar la recursividad 

def countdown(n):
    if n == 0:           # Caso base
        print("¡Despegue!")
        return
    else:                # Caso recursivo
        print(n)
        countdown(n - 1)

countdown(3)

