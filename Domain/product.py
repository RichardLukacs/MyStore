class Product:
    def __init__(self, product_id: int, name: str, producer: str, category: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.producer = producer
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self):
        return f'{str(self.product_id)}, {self.name}, {self.producer}, {self.category}, {self.price}, {self.stock}'


