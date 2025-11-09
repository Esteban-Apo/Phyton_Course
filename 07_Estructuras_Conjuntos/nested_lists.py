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