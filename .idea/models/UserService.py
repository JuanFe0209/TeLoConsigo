from Comprador import Comprador
from Notification import Notification
from Screen import Screen
from User import User
from WelcomeEmail import WelcomeEmail

class UserService:
    def __init__(self):
        self.users = []

    def create_user(self):
        user_id = input("ID: ")
        name = input("Nombre: ")
        identification = input("Identificación: ")
        address = input("Dirección: ")
        phone_number = input("Teléfono: ")
        email = input("Correo electrónico: ")

        if self.find_by_id(user_id):
            print("¡El ID ya está registrado!")
            return None

        customer_type = input("Tipo de cliente (1 para Comprador Ocasional, 2 para Comprador Mayorista): ")
        if customer_type == "1":
            customer_type = Comprador.Ocasional
        elif customer_type == "2":
            customer_type = Comprador.Mayorista
        else:
            print("¡Opción inválida!")
            return None

        new_user = User(user_id, name, identification, address, phone_number, email, customer_type)
        self.users.append(new_user)

        self.register_user(new_user)
        if new_user.comprador == Comprador.Ocasional:
            print("¡Usuario creado! Pronto tendrás acceso al catálogo web de productos tecnológicos")
        elif new_user.comprador == Comprador.Mayorista:
            print(f"¡Usuario creado! Correo de Bienvenida enviado a {email}")
        return new_user

    def register_user(self, user):
        print("Registrando usuario...")
        if user.comprador == Comprador.Mayorista:
            notification = WelcomeEmail()
            message = notification.send_message(user)
        else:
            notification = Screen()
            message = notification.send_message(user)

        return message

    def find_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def update_user(self, user_id, new_user):
        user = self.find_by_id(user_id)
        if user:
            print(f"Actualizando información del usuario {user.name}")
            user.name = new_user.get("name", user.name)
            user.identification = new_user.get("identification", user.identification)
            user.address = new_user.get("address", user.address)
            user.phone_number = new_user.get("phone_number", user.phone_number)
            user.email = new_user.get("email", user.email)
            user.comprador = new_user.get("comprador", user.comprador)
            print(f"¡Usuario actualizado! {user}")
        else:
            print("¡Usuario no encontrado!")

    def delete_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                print(f"Usuario con ID {user_id} eliminado.")
                return
        print("¡Usuario no encontrado!")
