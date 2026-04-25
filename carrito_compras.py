class CarritoCompras:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = {}

    def agregar(self, producto, precio):
        self.productos[producto] = precio

    def total(self):
        return sum(self.productos.values())

    def __str__(self):
        lineas = [f"Carrito de {self.cliente}:"]
        for producto, precio in self.productos.items():
            lineas.append(f"  - {producto}: ${precio:.2f}")
        lineas.append(f"Total: ${self.total():.2f}")
        return "\n".join(lineas)

    def __len__(self):
        return len(self.productos)


if __name__ == "__main__":
    carrito1 = CarritoCompras("Ana")
    carrito1.agregar("Laptop", 1200.00)
    carrito1.agregar("Mouse", 25.50)
    carrito1.agregar("Teclado", 45.00)

    carrito2 = CarritoCompras("Carlos")
    carrito2.agregar("Monitor", 350.00)
    carrito2.agregar("Auriculares", 80.00)

    print(carrito1)
    print(f"Cantidad de productos en el carrito de {carrito1.cliente}: {len(carrito1)}")
    print()
    print(carrito2)
    print(f"Cantidad de productos en el carrito de {carrito2.cliente}: {len(carrito2)}")
