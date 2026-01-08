from datetime import date

class Sale:
    def __init__(
        self,
        product_id: int,
        month: int,
        quantity: int,
        total_price: float,
        sale_date: date
    ):
        self.product_id = product_id
        self.month = month
        self.quantity = quantity
        self.total_price = total_price
        self.sale_date = sale_date
