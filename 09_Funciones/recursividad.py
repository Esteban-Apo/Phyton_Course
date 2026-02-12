#Uso de la serie Fibonacci para demostrar la recursividad 
def fib(n):
    if n < 1:
        return None
    if n < 3:      # casos base
        return 1
    return fib(n-1) + fib(n-2)   # caso recursivo


def countdown(n):
    if n == 0:           # Caso base
        print("¡Despegue!")
        return
    else:                # Caso recursivo
        print(n)
        countdown(n - 1)

countdown(3)

