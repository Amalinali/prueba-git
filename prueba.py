def sumar_precios(precio_amortiguador, precio_bujia):
    total = precio_amortiguador + precio_bujia
    return total

# Autollamada directa al ejecutar el script
resultado = sumar_precios(1200.50, 350.00)
print(f"El costo total de las piezas es: ${resultado}")