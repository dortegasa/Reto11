def IntroMatriz(Fil, Colum):
    Matriz1 = []  # Lista para almacenar la matriz
    for i in range(Fil):  # Iterar sobre las filas de la matriz
        Fila = []  # Lista para almacenar los elementos de cada fila
        for j in range(Colum):  # Iterar sobre las columnas de la matriz
            valor = int(input(f"Ingrese el elemento [{i}][{j}]: "))  # Solicitar al usuario el valor del elemento
            Fila.append(valor)  # Agregar el valor a la lista de la fila
        Matriz1.append(Fila)  # Agregar la lista de la fila a la matriz
    return Matriz1

def SumaColumnas(Matriz1, Column):
    Sum = 0  # Variable para almacenar la suma de los elementos de la columna
    for Fila in Matriz1:  # Iterar sobre las filas de la matriz
        if Column < len(Fila):  # Verificar si la columna está dentro del rango de la fila
            Sum += Fila[Column]  # Sumar el elemento de la columna a la variable de suma
    return Sum

Fil = int(input("Ingrese el número de filas de la matriz: "))  # Solicitar al usuario el número de filas de la matriz
Colum = int(input("Ingrese el número de columnas de la matriz: "))  # Solicitar al usuario el número de columnas de la matriz
Matriz1 = IntroMatriz(Fil, Colum)  # Llamar a la función para ingresar la matriz
ColumnaBrindada = int(input("Ingrese el número de columnas a sumar: "))  # Solicitar al usuario el número de columna a sumar
Result = SumaColumnas(Matriz1, ColumnaBrindada)  # Llamar a la función para sumar los elementos de la columna
print(f"La suma de la columna {ColumnaBrindada} es: {Result}")  # Imprimir el resultado de la suma
