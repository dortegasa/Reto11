def IntroMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Ingrese el elemento [{i}][{j}]: "))  # Se solicita al usuario que ingrese un elemento de la matriz
            fila.append(elemento)  # El elemento se agrega a la fila actual
        matriz.append(fila)  # La fila se agrega a la matriz
    return matriz

def MultiplicarMatriz(m1, m2):
    result = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m2[0])):
            elemento = 0
            for k in range(len(m2)):
                elemento += m1[i][k] * m2[k][j]  # Se realiza la multiplicación de los elementos correspondientes de m1 y m2
            fila.append(elemento)  # El elemento resultante se agrega a la fila
        result.append(fila)  # La fila se agrega al resultado
    return result

if __name__ == "__main__":
    filas = int(input("Ingrese el número de filas de las matrices: "))  # Se solicita al usuario el número de filas de las matrices
    columnas = int(input("Ingrese el número de columnas de las matrices: "))  # Se solicita al usuario el número de columnas de las matrices

    PrimerMatriz = IntroMatriz(filas, columnas)  # Se ingresa la primera matriz
    print("Matriz 1:", PrimerMatriz)  # Se imprime la primera matriz

    SegunMatriz = IntroMatriz(filas, columnas)  # Se ingresa la segunda matriz
    print("Matriz 2:", SegunMatriz)  # Se imprime la segunda matriz

    if len(PrimerMatriz[0]) != len(SegunMatriz):  # Se verifica si las matrices tienen las dimensiones adecuadas para la multiplicación
        print("Error: El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
    else:
        MatrizProducto = MultiplicarMatriz(PrimerMatriz, SegunMatriz)  # Se realiza el producto de las matrices

        print("El resultado del producto de las matrices es:")
        for fila in MatrizProducto:
            print(fila)  # Se imprime el producto de las matrices fila por fila