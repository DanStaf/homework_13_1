class Category:

    number_of_categories = 0
    unique_product_names = set()
    number_of_products_types = 0

    def __init__(self, name="", description="", goods=list()):

        self.name = name
        self.description = description
        self.__goods = goods

        Category.number_of_categories += 1
        self.add_products()

    def add_products(self):
        for good in self.__goods:
            Category.unique_product_names.add(good.get_name())

        Category.number_of_products_types = len(Category.unique_product_names)

    def add_product_in_category(self, product):
        self.__goods.append(product)

    def __repr__(self):
        return f'*Category:{self.name}*\n*Contains:{self.__goods}*\n'

    @property
    def list_of_goods(self):
        return [f"{each.name}, {each.price} руб. Остаток: {each.qty} шт." for each in self.__goods]


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

    @classmethod
    def new_product(cls, name, description, price, quantity):

        return cls(name, description, price, quantity)


######################
