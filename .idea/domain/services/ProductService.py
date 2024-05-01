from Product import Product
from enums.ProductCategory import ProductCategory

class ProductService:
    def __init__(self):

        self.products = []  # Lista para almacenar los productos

    def add_product(self):
       # Permite al usuario agregar un nuevo producto a la lista de productos.
        name = input("Nombre del producto: ")
        sku = input("SKU del producto: ")
        description = input("Descripción del producto: ")
        material = input("Material del producto: ")
        color = input("Color del producto: ")
        price = float(input("Precio del producto: "))
        category = self.choose_category()  # Elige la categoría del producto
        availability = int(input("Existencia disponible del producto: "))
        creation_date = input("Fecha de creación del producto: ")
        update_date = input("Fecha de actualización del producto: ")

        # Crea un nuevo objeto Product con los datos proporcionados y lo agrega a la lista de productos
        new_product = Product(name, sku, description, price, category, availability, creation_date, update_date, material, color)
        self.products.append(new_product)
        print("¡Producto agregado correctamente!")

    def choose_category(self):
        #Permite al usuario seleccionar la categoría del producto.
        while True:
            print("\nCategorías de producto:")
            for idx, category in enumerate(ProductCategory, start=1):
                print(f"{idx}. {category.value}")
            choice = input("Seleccione la categoría del producto: ")
            if choice.isdigit() and 1 <= int(choice) <= len(ProductCategory):
                return list(ProductCategory)[int(choice) - 1]
            else:
                print("¡Opción inválida!")

    def edit_product(self):
        # Permite al usuario editar un producto existente en la lista de productos.
        sku = input("SKU del producto a editar: ")
        product = self.find_product_by_sku(sku)  # Busca el producto por su SKU
        if product:
            print("Actualización de Producto")
            # Actualiza los atributos del producto con los nuevos valores proporcionados por el usuario
            product.name = input(f"Nuevo nombre ({product.name}): ") or product.name
            product.description = input(f"Nueva descripción ({product.description}): ") or product.description
            product.price = float(input(f"Nuevo precio ({product.price}): ") or product.price)
            product.category = self.choose_category()  # Elige la nueva categoría del producto
            product.availability = int(input(f"Nueva existencia disponible ({product.availability}): ") or product.availability)
            product.creation_date = input(f"Nueva fecha de creación ({product.creation_date}): ") or product.creation_date
            product.update_date = input(f"Nueva fecha de actualización ({product.update_date}): ") or product.update_date
            product.material = input(f"Nuevo material ({product.material}): ") or product.material
            product.color = input(f"Nuevo color ({product.color}): ") or product.color
            print("¡Producto actualizado correctamente!")
        else:
            print("¡Producto no encontrado!")

    def find_product_by_sku(self, sku):
       # Busca un producto por su SKU en la lista de productos.
        for product in self.products:
            if product.sku == sku:
                return product
        return None

    def delete_product(self):
       # Permite al usuario eliminar un producto de la lista de productos.
        sku = input("SKU del producto a eliminar: ")
        product = self.find_product_by_sku(sku)  # Busca el producto por su SKU
        if product:
            self.products.remove(product)  # Elimina el producto de la lista
            print(f"¡Producto con SKU {sku} eliminado!")
        else:
            print("¡Producto no encontrado!")
