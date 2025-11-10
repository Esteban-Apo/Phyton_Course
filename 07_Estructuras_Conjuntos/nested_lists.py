#Listas bidimencionales 

def matrices():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(matriz[0])      # Muestra la primera fila: [1, 2, 3]
    print(matriz[0][1])   # Muestra el elemento en fila 0, columna 1 → 2


    for row in matriz:  #Recorrer las filas de una Matriz (Lista anidada)
        print(row)

    for row in matriz: #Recorrer los valores de cada Fila
        for value in row:
            print(value)

def notas_estudiantes():
    notas = [
        ["Ana", [4.5, 3.8, 4.0]],
        ["Luis", [3.0, 3.5, 3.2]],
        ["Sofía", [5.0, 4.8, 4.9]]
        ]

    for estudiante in notas:
        nombre = estudiante[0]
        calificaciones = estudiante[1]
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"{nombre} tiene un promedio de {promedio:.2f}")


#Aplicaciónes avanzadas de las listas 

#Listas en Rebandas y  indices negativos 
def negative_list():
    my_negative_list = [1,2,3,4,5,6]
    my_negative_list[-1]   # 6  (último)
    my_negative_list[-2]   # 5  (penúltimo)
    print(my_negative_list[-6]) #Primer valor, Ultimo indice negativo 

#Slices (Rebanadas), permite sub-listar u obtener una parte de una lista. 
def slices():
    my_list = [10, 20, 30, 40, 50]
    print(my_list[1:4]) #->[20, 30, 40]

#slices()
def slices_with_negative_indices():
    my_list = [10, 20, 30, 40, 50]
    print(my_list[-5:-2]) #[10, 20, 30]

slices_with_negative_indices()
