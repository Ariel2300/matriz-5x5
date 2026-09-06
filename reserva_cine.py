"""
Tarea Semana 12: Reserva de un asiento en sala de cine
Unidad 3. Arreglos N-Dimensionales - Tema 3.2.2

Gestiona la reserva de un asiento en una sala de cine de 3 filas y 4
columnas.
"""

NUM_FILAS = 3
NUM_COLUMNAS = 4

# Crear la matriz con todos los asientos libres.
asientos = []
for fila in range(NUM_FILAS):
	fila_asientos = []
	for columna in range(NUM_COLUMNAS):
		fila_asientos.append(0)
	asientos.append(fila_asientos)

# Solicitar la ubicación del asiento.
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

if 0 <= fila < NUM_FILAS and 0 <= columna < NUM_COLUMNAS:
	if asientos[fila][columna] == 1:
		print("Aviso: ese asiento ya estaba reservado.")
	else:
		asientos[fila][columna] = 1
		print("Asiento reservado con éxito.")
else:
	print("Error: la fila o la columna ingresada está fuera de rango.")

# Mostrar el estado completo de la sala.
print("\nEstado de la sala:")
for i in range(NUM_FILAS):
	for j in range(NUM_COLUMNAS):
		print(asientos[i][j], end=" ")
	print()
