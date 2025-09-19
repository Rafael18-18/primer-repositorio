def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a un monto total.
    :param monto_total: float, el valor de la compra
    :param porcentaje_descuento: float, porcentaje de descuento (por defecto 10%)
    :return: float, el monto del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
# 1 Llamada soLo con el monto (usa 10% por defecto)
monto1 = 100
descuento1 = calcular_descuento(monto1)
print(f"Compra: ${monto1}, Descuento: ${descuento1}, Total a pagar: ${monto1 - descuento1}")

# 2 Llamada con monto y porcentaje específico
monto2 = 200
descuento2 = calcular_descuento(monto2, 15)
print(f"Compra: ${monto2}, Descuento: ${descuento2}, Total a pagar: ${monto2 - descuento2}")
