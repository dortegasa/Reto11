def IntroMatriz(Fil, Colum):
    Matriz1 = []  # Lista para almacenar la matriz
    for i in range(Fil):  # Iterar sobre las filas de la matriz
        Fila = []  # Lista para almacenar los elementos de cada fila
        for j in range(Colum):  # Iterar sobre las columnas de la matriz
            valor = int(input(f"Ingrese el elemento [{i}][{j}]: "))  # Solicitar al usuario el valor del elemento
            Fila.append(valor)  # Agregar el valor a la lista de la fila
        Matriz1.append(Fila)  # Agregar la lista de la fila a la matriz
    return Matriz1

def SumaFilas(Matriz1, Fila):
    Sum = 0  # Variable para almacenar la suma de los elementos de la fila
    if Fila < len(Matriz1):  # Verificar si la fila está dentro del rango de la matriz
        Sum = sum(Matriz1[Fila])  # Sumar los elementos de la fila utilizando la función sum()
    return Sum

Fil = int(input("Ingrese el número de filas de la matriz: "))  # Solicitar al usuario el número de filas de la matriz
Colum = int(input("Ingrese el número de columnas de la matriz: "))  # Solicitar al usuario el número de columnas de la matriz
Matriz1 = IntroMatriz(Fil, Colum)  # Llamar a la función para ingresar la matriz
FilaBrindada = int(input("Ingrese el número de fila a sumar: "))  # Solicitar al usuario el número de fila a sumar
Result = SumaFilas(Matriz1, FilaBrindada)  # Llamar a la función para sumar los elementos de la fila
print(f"La suma de la fila {FilaBrindada} es: {Result}")  # Imprimir el resultado de la suma
