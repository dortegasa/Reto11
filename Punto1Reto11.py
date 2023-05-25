def IntroMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Ingrese el elemento [{i}][{j}]: "))  # Se solicita al usuario que ingrese un elemento de la matriz
            fila.append(elemento)  # El elemento se agrega a la fila actual
        matriz.append(fila)  # La fila se agrega a la matriz
    return matriz

def SumarMatriz(m1, m2):
    Result = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            fila.append(m1[i][j] + m2[i][j])  # Se suma el elemento correspondiente de m1 y m2 y se agrega a la fila
        Result.append(fila)  # La fila se agrega al resultado
    return Result

def RestarMatriz(m1, m2):
    Result = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            fila.append(m1[i][j] - m2[i][j])  # Se resta el elemento correspondiente de m1 y m2 y se agrega a la fila
        Result.append(fila)  # La fila se agrega al resultado
    return Result

if __name__ == "__main__":
    filas = int(input("Ingrese el número de filas de las matrices: "))  # Se solicita al usuario el número de filas de las matrices
    columnas = int(input("Ingrese el número de columnas de las matrices: "))  # Se solicita al usuario el número de columnas de las matrices

    PrimerMatriz = IntroMatriz(filas, columnas)  # Se ingresa la primera matriz
    print("matriz 1:", PrimerMatriz)  # Se imprime la primera matriz

    SegunMatriz = IntroMatriz(filas, columnas)  # Se ingresa la segunda matriz
    print("Matriz 2", SegunMatriz)  # Se imprime la segunda matriz

    if len(PrimerMatriz) != len(SegunMatriz) or len(PrimerMatriz[0]) != len(SegunMatriz[0]):
        print("Error: Las matrices deben tener las mismas dimensiones para realizar la operación.")  # Se verifica si las matrices tienen las mismas dimensiones
    else:
        MatrizSuma = SumarMatriz(PrimerMatriz, SegunMatriz)  # Se realiza la suma de las matrices
        MatrizResta = RestarMatriz(PrimerMatriz, SegunMatriz)  # Se realiza la resta de las matrices

        print("El resultado de la suma de las matrices es:")
        for fila in MatrizSuma:
            print(fila)  # Se imprime la suma de las matrices fila por fila

        print("El resultado de la resta de las matrices es:")
        for fila in MatrizResta:
            print(fila)  # Se imprime la resta de las matrices fila por fila