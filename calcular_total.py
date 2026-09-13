"""
Tarea práctica: crear una función basada en un problema de la vida real
Tema: Definición y uso de funciones en Python

Problema elegido: calcular el total de una compra en una tienda,
a partir del precio de un producto y la cantidad que lleva el cliente.

Autor: Ariel Alejandro Álvarez Chauca
"""


def calcularTotal(precio, cantidad):
    """
    Calcula el total a pagar por una compra.

    Parámetros:
        precio (float): precio unitario del producto.
        cantidad (int): cantidad de unidades que lleva el cliente.

    Retorna:
        float: el total de la compra (precio * cantidad).
    """
    total = precio * cantidad
    return total


if __name__ == "__main__":
    # Datos de ejemplo (equivalentes al pseudocódigo de la guía)
    precio = 10
    cantidad = 3

    resultado = calcularTotal(precio, cantidad)
    print(f"El total de la compra es: {resultado}")

    # Prueba adicional con datos ingresados por el usuario
    precio_usuario = float(input("Ingrese el precio del producto: "))
    cantidad_usuario = int(input("Ingrese la cantidad de productos: "))

    total_usuario = calcularTotal(precio_usuario, cantidad_usuario)
    print(f"El total a pagar es: {total_usuario}")
    