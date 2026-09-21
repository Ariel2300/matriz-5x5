"""
Tarea: Programación Básica - Funciones con parámetros y retorno de valores
Autor: Ariel Alejandro Álvarez Chauca
Universidad Estatal Amazónica - Tecnologías de la Información

Problema: Calcular el precio total de una compra aplicando
un descuento y el IVA del 15% vigente en Ecuador.
"""

IVA = 0.15  # 15% de IVA en Ecuador


def calcular_precio_total(precio_unitario, cantidad, descuento):
    """
    Parámetros de entrada:
        precio_unitario (float): precio de un solo producto
        cantidad (int): número de productos comprados
        descuento (float): porcentaje de descuento (ej. 10 para 10%)
    Retorna:
        float: valor final a pagar con descuento e IVA incluido
    """
    subtotal = precio_unitario * cantidad
    valor_descuento = subtotal * (descuento / 100)
    base_imponible = subtotal - valor_descuento
    total = base_imponible + (base_imponible * IVA)
    return round(total, 2)


# Programa principal
print("=====================================")
print("   CALCULADORA DE COMPRA - TIENDA    ")
print("=====================================")

producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio unitario ($): "))
cantidad = int(input("Ingrese la cantidad: "))
descuento = float(input("Ingrese el descuento (%): "))

# Llamada a la función
total_a_pagar = calcular_precio_total(precio, cantidad, descuento)

# Mostrar el resultado en pantalla
print("\n------------ FACTURA ------------")
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Precio unitario: $", precio)
print("Descuento aplicado:", descuento, "%")
print("IVA aplicado: 15 %")
print("TOTAL A PAGAR: $", total_a_pagar)
print("---------------------------------")
