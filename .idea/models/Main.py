from UserService import UserService

def main():
    user_service = UserService()

    while True:
        print("\nMenú de Gestión de Usuarios")
        print("1. Registrar usuario")
        print("2. Actualizar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")
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
                new_comprador = input(f"Nuevo tipo de comprador ({user.comprador}): ") or user.comprador
                user_service.update_user(user_id, {
                    "name": new_name,
                    "identification": new_identification,
                    "address": new_address,
                    "phone_number": new_phone_number,
                    "email": new_email,
                    "comprador": new_comprador
                })
        elif option == "3":
            user_id = input("ID del usuario a eliminar: ")
            user_service.delete_user(user_id)
        elif option == "4":
            print("Saliendo...")
            break
        else:
            print("¡Opción inválida!")

if __name__ == "__main__":
    main()
