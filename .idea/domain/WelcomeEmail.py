from Notification import Notification

class WelcomeEmail(Notification):
    def send_message(self, user):
        return f"Bienvenido a nuestra plataforma de compras mayoristas, {user.name}! Lea y acepte nuestros términos y condiciones para comenzar a realizar pedidos."
