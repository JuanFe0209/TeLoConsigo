from enums.Comprador import Comprador
from Notification import Notification
from Screen import Screen
from WelcomeEmail import WelcomeEmail
from User import User

class UserService:
    def __init__(self):
        self.users = []  # Inicializamos una lista para almacenar los usuarios

        # Mapeo de tipos de cliente a clases de notificación
        self.notification_handlers = {
            "1": Screen(),  # Asignamos la clase Screen para el tipo de cliente 1
            "2": WelcomeEmail()  # Asignamos la clase WelcomeEmail para el tipo de cliente 2
        }

    def create_user(self):
        # Solicitamos la información del nuevo usuario al usuario
        user_id = input("ID: ")
        name = input("Nombre: ")
        identification = input("Identificación: ")
        address = input("Dirección: ")
        phone_number = input("Teléfono: ")
        email = input("Correo electrónico: ")

        # Verificamos si el ID ya está registrado
        if self.find_by_id(user_id):
            print("¡El ID ya está registrado!")
            return None

        # Solicitamos el tipo de cliente al usuario
        customer_type = input("Tipo de cliente (1 para Comprador Ocasional, 2 para Comprador Mayorista): ")
        notification_handler = self.notification_handlers.get(customer_type)  # Obtenemos el manejador de notificación correspondiente
        if notification_handler is None:
            print("¡Opción inválida!")
            return None

        # Convertimos el tipo de cliente a un valor de la enumeración
        customer_type = Comprador.Ocasional if customer_type == "1" else Comprador.Mayorista

        # Creamos una instancia del nuevo usuario
        new_user = User(user_id, name, identification, address, phone_number, email, customer_type)
        self.users.append(new_user)  # Agregamos el nuevo usuario a la lista de usuarios

        # Registramos al nuevo usuario utilizando el manejador de notificación correspondiente
        self.register_user(new_user, notification_handler)
        return new_user

    def update_user(self, user_id, new_data):
        # Buscamos al usuario por su ID
        user = self.find_by_id(user_id)
        if user:
            print(f"Actualizando información del usuario {user.name}")
            # Actualizamos los datos del usuario con los nuevos datos proporcionados
            for key, value in new_data.items():
                setattr(user, key, value)
            print(f"¡Usuario actualizado! {user}")
        else:
            print("¡Usuario no encontrado!")

    def register_user(self, user, notification_handler):
        # Registramos al usuario utilizando el manejador de notificación proporcionado
        print("Registrando usuario...")
        message = notification_handler.send_message(user)
        print(message)

    def find_by_id(self, user_id):
        # Buscamos al usuario por su ID en la lista de usuarios
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def delete_user(self, user_id):
        # Buscamos al usuario por su ID y lo eliminamos de la lista de usuarios
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                print(f"Usuario con ID {user_id} eliminado.")
                return
        print("¡Usuario no encontrado!")