class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self._precio = None
        self._stock = None
        self.precio = precio    # usa el setter
        self.stock = stock      # usa el setter

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = valor

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = valor

    @property
    def inventario(self):
        return f'{self.nombre} - Precio: ${self.precio}, Stock: {self.stock} unidades'

    @inventario.deleter
    def inventario(self):
        print(f'Eliminando información del producto: {self.nombre}')
        self._precio = None
        self._stock = None

# --- Uso de ejemplo ---
producto = Producto("Laptop", 1500, 10)
print(producto.inventario)

# Actualización válida
producto.precio = 1800
producto.stock = 5
print(producto.inventario)

# Eliminación del inventario
del producto.inventario
print(producto.inventario)  # Ahora mostrará "None"
