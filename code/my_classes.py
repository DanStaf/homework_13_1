class Category:

    number_of_categories = 0
    products_types = set()
    number_of_products_types = 0

    def __init__(self, name="", description="", goods=list()):

        self.name = name
        self.description = description
        self.goods = goods

        Category.number_of_categories += 1
        self.add_products()

    def add_products(self):
        Category.products_types.add(self.goods)
        Category.number_of_products_types = len(Category.products_types)


class Product:

    def __init__(self, name="", description="", price=0.0, qty=0):

        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

######################
