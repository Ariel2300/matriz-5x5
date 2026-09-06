# Reserva de un asiento en sala de cine

**Estudiante:** [Ariel Alejandro Alvarez Chauca]

## Objetivo del programa

Gestionar la reserva de asientos de una sala de cine pequeña, organizada en
3 filas y 4 columnas (12 asientos en total). El programa representa la sala
mediante una matriz (lista de listas) en la que cada asiento tiene un valor:

- `0` = asiento libre
- `1` = asiento reservado

El usuario indica la fila y la columna del asiento que desea reservar, y el
programa actualiza y muestra el estado completo de la sala en formato de
tabla, usando bucles anidados para recorrer la matriz.

## Cómo ejecutarlo

1. Asegúrate de tener Python 3 instalado.
2. Ejecuta el archivo desde la terminal:

```bash
   python reserva_cine.py
```

3. Ingresa la fila (0 a 2) y la columna (0 a 3) del asiento que deseas
   reservar cuando el programa lo solicite.
4. El programa mostrará el estado final de la sala como una tabla de
   3 filas por 4 columnas, con ceros y unos.

## Ejemplo de ejecución

```
Ingrese fila (0 a 2): 1
Ingrese columna (0 a 3): 2
Asiento reservado con éxito.

Estado de la sala:
0 0 0 0
0 0 1 0
0 0 0 0
```