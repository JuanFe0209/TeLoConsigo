from services.UserService import UserService
from services.ProductService import ProductService

def main():
    user_service = UserService()
    product_service = ProductService()

    while True:
        print("\nMenú Principal")
        print("1. Gestión de Usuarios")
        print("2. Gestión de Productos")
        print("3. Salir")
        option = input("Seleccione una opción: ")

        if option == "1":
            manage_users(user_service)
        elif option == "2":
            manage_products(product_service)
        elif option == "3":
            print("Saliendo...")
            break
        else:
            print("¡Opción inválida!")

def manage_users(user_service):
    while True:
        print("\nMenú de Gestión de Usuarios")
        print("1. Registrar usuario")
        print("2. Actualizar usuario")
        print("3. Eliminar usuario")
        print("4. Volver al menú principal")
        option = input("Seleccione una opción: ")

        if option == "1":
            user_service.create_user()
        elif option == "2":
            user_id = input("ID del usuario a actualizar: ")
            user = user_service.find_by_id(user_id)
            if user:
                print("Actualización de Usuario")
                new_name = input(f"Nuevo nombre ({user.name}): ") or user.name
                new_identification = input(f"Nueva identificación ({user.identification}): ") or user.identification
                new_address = input(f"Nueva dirección ({user.address}): ") or user.address
                new_phone_number = input(f"Nuevo teléfono ({user.phone_number}): ") or user.phone_number
                new_email = input(f"Nuevo correo electrónico ({user.email}): ") or user.email
                user_service.update_user(user_id, {
                    "name": new_name,
                    "identification": new_identification,
                    "address": new_address,
                    "phone_number": new_phone_number,
                    "email": new_email
                })
            else:
                print("¡Usuario no encontrado!")
        elif option == "3":
            user_id = input("ID del usuario a eliminar: ")
            user_service.delete_user(user_id)
        elif option == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("¡Opción inválida!")

def manage_products(product_service):
    while True:
        print("\nMenú de Gestión de Productos")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Consultar producto por SKU")
        print("4. Eliminar producto")
        print("5. Volver al menú principal")
        option = input("Seleccione una opción: ")

        if option == "1":
            product_service.add_product()
        elif option == "2":
            product_service.edit_product()
        elif option == "3":
            sku = input("Ingrese el SKU del producto a consultar: ")
            product_service.get_product_by_sku(sku)
        elif option == "4":
            product_service.delete_product()
        elif option == "5":
            print("Volviendo al menú principal...")
            break
        else:
            print("¡Opción inválida!")

if __name__ == "__main__":
    main()
