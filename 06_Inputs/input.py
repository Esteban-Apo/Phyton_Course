#Funcion que se utiliza para pedirle datos al usuario
nombre = input("Escribre tu nombre: ") #los Imputs simpre convierten los valores en cadenas de texto.
print(nombre)


#Si se necesita un numeor, es necesario pasarlo a Int o a Float

numero = int(input("Mutiplicador de numeros x2: ")) #Es necesario que el numero se convierte en un Int o Float
numero *= 2
print(f"El valor multiplicado por dos es:  {numero} ")