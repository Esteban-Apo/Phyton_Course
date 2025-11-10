#Crea una lista T que contenga 3 listas anidadas "i for i in range(3)"
#y a su vez que los valores que entrege la lista "i" se reste con el valor 3
#Generando asi una lista inversa.


#Lista comprimida
t = [[3 - i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)

t = [  #lista bidimencional generada por la varible t
    [3, 2, 1],  # j = 0
    [3, 2, 1],  # j = 1
    [3, 2, 1]   # j = 2
]




#Lista no comprimida 
t = []
for j in range(3):        # bucle externo
    fila = []
    for i in range(3):    # bucle interno
        fila.append(3 - i)
    t.append(fila)

