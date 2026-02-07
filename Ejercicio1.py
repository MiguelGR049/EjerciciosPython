ventas = [
    ("Ana", "Enero", "Laptop", 2, 15000),
    ("Luis", "Enero", "Mouse", 10, 250),
    ("Ana", "Febrero", "Laptop", 1, 15000),
    ("Luis", "Febrero", "Teclado", 5, 800),
    ("Ana", "Enero", "Mouse", 3, 250)
]

# Calcular total de ingresos por empleados
def calcularIngresos(ventas):
    ingresos_empleados = {}
    for venta in ventas:
        empleado, mes, producto, cantidad, precio_unitario = venta
        total_venta = cantidad * precio_unitario
        if empleado in ingresos_empleados:
            ingresos_empleados[empleado] += total_venta
        else:
            ingresos_empleados[empleado] = total_venta
    return ingresos_empleados

# Obtener el conjunto con los productos unicos vendidos
def productosUnicos(ventas):
    productos = set()
    for venta in ventas:
        producto = venta[2]
        productos.add(producto)
    return productos
# Crear un diccionario con el total de ingresos por mes
def ingresosMes():
    ingresos_por_mes = {}
    for venta in ventas:
        mes = venta[1]
        cantidad = venta[3]
        precio_unitario = venta[4]
        total_venta = cantidad * precio_unitario
        if mes in ingresos_por_mes:
            ingresos_por_mes[mes] += total_venta
        else:
            ingresos_por_mes[mes] = total_venta
    return ingresos_por_mes
# Determinar que empleado genero mayores ingresos
def empleadoMayorIngreso(ingresos_empleados):
    mayor_ingreso = 0
    empleado_mayor = ""
    for empleado, ingreso in ingresos_empleados.items():
        if ingreso > mayor_ingreso:
            mayor_ingreso = ingreso
            empleado_mayor = empleado
    return empleado_mayor, mayor_ingreso

print(f"Total de ingresos de Ana: {calcularIngresos(ventas)['Ana']}")
print(f"Total de ingresos de Luis: {calcularIngresos(ventas)['Luis']}")
print(" ")
print(f"Productos unicos vendidos: {productosUnicos(ventas)}")
print(" ")
print(f"Ingresos de Enero: {ingresosMes()['Enero']}")
print(f"Ingresos de Febrero: {ingresosMes()['Febrero']}")
print(" ")
print(f"El empleado con mayor ingreso es: {empleadoMayorIngreso(calcularIngresos(ventas))[0]}")