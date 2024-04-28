from Notification import Notification

class Screen(Notification):
    def send_message(self, user):
        return f"¡Usuario {user.name} registrado correctamente! Pronto tendrás acceso al catálogo de productos de tecnología."
