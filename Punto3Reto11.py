def IngreMatriz(Fil, Column):
    matriz = []
    for i in range(0, Fil):
        fila = []
        print("Ingrese los valores que tendrá la fila " + str(i))
        for j in range(0, Column):
            Val = float(input())  # Se solicita al usuario ingresar el valor para cada posición de la matriz
            fila.append(Val)  # El valor ingresado se agrega a la fila
        matriz.append(fila)  # La fila se agrega a la matriz
    return matriz

def MatrizTransp(Fil, Column, Matriz1):
    Transp = []
    for x in range(0, Column):
        lista = []
        for m in range(0, Fil):
            lista.append(Matriz1[m][x])  # Se transponen los elementos de la matriz y se guardan en una nueva lista
        Transp.append(lista)  # La lista transpuesta se agrega a la matriz de transposición
    return Transp

if __name__ == "__main__":
    print("Introduzca los valores por fila para la matriz")
    Fil = int(input("Especifique el número de filas que tendrá la primera matriz: "))  # Se solicita al usuario el número de filas de la matriz
    Column = int(input("Especifique el número de columnas que tendrá la primera matriz: "))  # Se solicita al usuario el número de columnas de la matriz

    Matriz1 = IngreMatriz(Fil, Column)  # Se ingresa la matriz
    for i in range(0, Fil):
        print(Matriz1[i])  # Se imprime la matriz ingresada fila por fila

    Matriz2 = MatrizTransp(Fil, Column, Matriz1)  # Se calcula la transposición de la matriz
    print("La transposición de la matriz es: ")
    for i in range(0, Column):
        print(Matriz2[i])  # Se imprime la matriz transpuesta fila por fila
