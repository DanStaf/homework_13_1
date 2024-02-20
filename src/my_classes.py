class Category:

    number_of_categories = 0
    unique_product_names = set()
    number_of_products_types = 0

    def __init__(self, name="", description="", goods=list()):

        self.name = name
        self.description = description
        self.goods = goods

        Category.number_of_categories += 1
        self.add_products()

    def add_products(self):
        for good in self.goods:
            Category.unique_product_names.add(good.get_name())

        Category.number_of_products_types = len(Category.unique_product_names)

    def __repr__(self):
        return f'*Category:{self.name}*\n*Contains:{self.goods}*\n'


class Product:

    def __init__(self, name="", description="", price=0.0, qty=0):

        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

    def __repr__(self):
        return f'/Product:{self.name},{self.qty}pcs/'

    def get_name(self):
        return self.name

######################
