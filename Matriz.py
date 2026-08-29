# Declaración de la matriz de 3x3 con números enteros
matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

# Recorrido de la matriz utilizando ciclos anidados
print("Valores de la matriz:")
for i in range(3):
    for j in range(3):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")