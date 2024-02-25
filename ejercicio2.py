class Producto:
    nombre=None
    codigo=None
    def __init__ (self, nombre, codigo):
        self.nombre=nombre
        self.codigo=codigo
    def __str__ (self):
        return f"Producto {self.nombre} con codigo {self.codigo}"

producto1=Producto("aceite", "PERU-00001-2024")
product= str(producto1)
print(product)


    
