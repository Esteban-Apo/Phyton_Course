#Un método es una función que pertenece a un objeto,
cadena1 = "Hola mi nombre es esteban"
cadena2 = "Holalalla"
cadena3 = "232324"
cadena_comas = "hola,como estas,tamo,laura"

#Convierte en mayusculas
mayorC = cadena1.upper()

#Convierte en minusculas 
menorC = cadena2.lower()

#Primer letra mayuscula
primer_letra_mayus = cadena2.capitalize()

#Busca un valor concreto de una cadena, si no encuetra resultados arroja un -1
busqueda_x_find = cadena1.find("H")

#Busca un valor concreto de una cadena, si no encuentra resultados arroja una EXEPCIÓN
busqueda_x_index = cadena2.index("l")

#Independientemente de ser una cadena de texto, este metodo verifica si esta cadena es numerica o no
is_numerico = cadena3.isnumeric()

#Si es alfa numerico es true (alfa numerico == letras de A a la Z)
is_alfa_numerico = cadena2.isalpha()

#Busca un valor de una cadena, devuelve la cantidad de veces que este valor se repite
counter_character = cadena2.count("a")
print(counter_character)

#Remplaza un valor de una cadena, por otro valor
cadena_nueva = cadena1.replace("esteban", "Laura")
print(cadena_nueva)

#Separa los valores dados, en base a un caracter dado
cadena_separada = cadena_comas