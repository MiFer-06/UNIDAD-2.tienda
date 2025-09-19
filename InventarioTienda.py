class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f'{self.nombre} - Precio: ${self.precio} - Cantidad: {self.cantidad}'

class InventarioTienda:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            print("Error: El precio y la cantidad deben ser valores positivos.")
            return
        
        if nombre in self.productos:
            self.productos[nombre].cantidad += cantidad
        else:
            self.productos[nombre] = Producto(nombre, precio, cantidad)
        print(f'Producto {nombre} agregado/actualizado correctamente.')

    def vender_producto(self, nombre, cantidad):
        if nombre not in self.productos:
            print("Error: El producto no existe en el inventario.")
            return
        
        if cantidad <= 0:
            print("Error: La cantidad a vender debe ser un valor positivo.")
            return

        producto = self.productos[nombre]
        if producto.cantidad < cantidad:
            print("Error: No hay suficiente stock para realizar la venta.")
            return
        
        producto.cantidad -= cantidad
        print(f'Venta realizada: {cantidad} unidades de {nombre}.')

        if producto.cantidad == 0:
            del self.productos[nombre]
            print(f'El producto {nombre} se ha agotado y fue eliminado del inventario.')

    def ver_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("Inventario actual:")
        for producto in self.productos.values():
            print(producto)

    def producto_mas_caro(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        producto_caro = max(self.productos.values(), key=lambda p: p.precio)
        print(f'Producto más caro: {producto_caro.nombre} - Precio: ${producto_caro.precio}')


def main():
    inventario = InventarioTienda()

    while True:
        print("\n--- Menú ---")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Ver inventario")
        print("4. Consultar producto más caro")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad: "))
            except ValueError:
                print("Error: Precio debe ser número decimal y cantidad número entero.")
                continue
            inventario.agregar_producto(nombre, precio, cantidad)

        elif opcion == '2':
            nombre = input("Nombre del producto a vender: ")
            try:
                cantidad = int(input("Cantidad a vender: "))
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")
                continue
            inventario.vender_producto(nombre, cantidad)

        elif opcion == '3':
            inventario.ver_inventario()

        elif opcion == '4':
            inventario.producto_mas_caro()

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
