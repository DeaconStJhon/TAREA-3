class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

class Catalogo:
    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)

    def mostrar_productos(self):
        for producto in self.lista_productos:
            print(f"Nombre: {producto.nombre}, Código: {producto.codigo}")

catalogo = Catalogo()
producto1 = Producto("Filtro de aceite", "PERU-00001")
producto2 = Producto("Batería", "USA-00002")

catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)

catalogo.mostrar_productos()