class Product:
    def __init__(self, name, sku, description, price, category, availability, creation_date=None, update_date=None,
                 material=None, color=None, images=None, variations=None):
        self.name = name
        self.sku = sku
        self.description = description
        self.price = price
        self.category = category
        self.availability = availability
        self.creation_date = creation_date
        self.update_date = update_date
        self.material = material
        self.color = color
        self.images = images or []
        self.variations = variations or []
