inventario = [
    {"producto": "Laptop", "categoria": "Electrónica", "stock": 5},
    {"producto": "Mouse", "categoria": "Electrónica", "stock": 25},
    {"producto": "Silla", "categoria": "Muebles", "stock": 2},
    {"producto": "Escritorio", "categoria": "Muebles", "stock": 0}
]

# Crear un diccionario donde la clave sea la categoría y el valor una lista de productos.
def productosPorCategoria(inventario):
    categorias = {}
    for item in inventario:
        categoria = item["categoria"]
        producto = item["producto"]
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(producto)
    return categorias
# Obtener un conjunto de productos agotados.
def productosAgotados(inventario):
    agotados = set()
    for item in inventario:
        if item["stock"] == 0:
            agotados.add(item["producto"])
    return agotados
# Generar una tupla con los productos cuyo stock sea menor a 5.
def productosBajoStock(inventario):
    bajo_stock = []
    for item in inventario:
        if item["stock"] < 5:
            bajo_stock.append(item["producto"])
    return tuple(bajo_stock)
# Calcular el total de productos por categoría.
def totalProductosPorCategoria(inventario):
    total_por_categoria = {}
    for item in inventario:
        categoria = item["categoria"]
        if categoria in total_por_categoria:
            total_por_categoria[categoria] += 1
        else:
            total_por_categoria[categoria] = 1
    return total_por_categoria

print(f"Productos por categoría: {productosPorCategoria(inventario)}")
print(" ")
print(f"Productos agotados: {productosAgotados(inventario)}")
print(" ")
print(f"Productos con stock menor a 5: {productosBajoStock(inventario)}")
print(" ")
print(f"Total de productos por categoría: {totalProductosPorCategoria(inventario)}")