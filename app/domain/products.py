class Product:
    def __init__(
        self,
        product_id: int,
        name: str,
        price: float,
        category_id: int,
        description: str,
        brand: str
    ):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category_id = category_id
        self.description = description
        self.brand = brand
