class Product:

    def __init__(self, name: str, description: str, price: float, qty: int):
        """

        :param name: имя продукта
        :param description: описание продукта
        :param price: цена продукта
        :param qty: количество продукта
        """

        self.name = name
        self.description = description
        self.__price = price
        self.qty = qty

    def __repr__(self):
        return f'/Product:{self.name},{self.qty}pcs/'

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.qty} шт.'

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError('Можно складывать товары только из одинаковых классов продуктов')

        return self.price * self.qty + other.price * other.qty

    def get_name(self):
        return self.name

    @classmethod
    def new_product(cls, product_list=None, **product_data):

        """product_data = {
            "name": "apple",
            "description": "fruits",
            "price": 100.00,
            "qty": 3
        }"""

        # если получили список, ищем совпадающий продукт
        if product_list:
            # ищем совпадающий продукт по имени
            for product in product_list:
                if product.name == product_data['name']:
                    # если нашли, складываем количество
                    # если нашли, выбираем наибольшую цену
                    product.qty += product_data['qty']
                    if product.price < product_data['price']:
                        product.price = product_data['price']

                    # возвращаем обновлённый продукт
                    return product

            # если не нашли совпадающий продукт:
        # если не получили список и не искали:

        # возвращаем новый продукт
        return cls(**product_data)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):

        if price <= 0:
            print("Некорректный ввод. Введённая цена должа быть больше 0")
        else:
            if self.__price:
                if price < self.__price:
                    user_confirmation = input("Подтвердите снижение цены"
                                              " y (значит yes) или нажмите n"
                                              " (значит no) для отмены действия.")
                    if user_confirmation == 'y':
                        self.__price = price
                    #else: pass
                else:
                    self.__price = price
            else:
                self.__price = price

    @price.deleter
    def price(self):
        self.__price = None


class Category:

    number_of_categories = 0
    unique_product_names = set()
    number_of_products_types = 0

    def __init__(self, name: str, description: str, goods: list):
        """

        :param name: имя категории
        :param description: описание категории
        :param goods: список объектов класса Product
        """

        self.name = name
        self.description = description
        self.__goods = goods

        Category.number_of_categories += 1
        self.add_products()

    def add_products(self):
        for good in self.__goods:
            Category.unique_product_names.add(good.get_name())

        Category.number_of_products_types = len(Category.unique_product_names)

    def add_product_in_category(self, product: Product):
        self.__goods.append(product)

    def __repr__(self):
        return f'*Category:{self.name}*\n*Contains:{self.__goods}*\n'

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        qty = 0
        for each in self.__goods:
            qty += each.qty
        return qty

    @property
    def list_of_goods(self):
        return [str(each) for each in self.__goods]


class CategoryIter:

    def __init__(self, category):
        """

        :param category: объект класса Category

        :attr goods: список товаров в строковом виде (можно изменить если будет нужно)
        """
        self.goods = category.list_of_goods

    def __len__(self):
        return len(self.goods)

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        if self.current_value + 1 < len(self):
            self.current_value += 1
            return self.goods[self.current_value]
        else:
            raise StopIteration


class Smartphone(Product):
    """class Smartphone is child of class Product"""

    def __init__(self, name: str, description: str, price: float, qty: int,
                 freq: float, model: str, ram: int, color: str):

        super().__init__(name, description, price, qty)
        self.freq = freq
        self.model = model
        self.ram = ram
        self.color = color


class GreenGrass(Product):
    """class GreenGrass is child of class Category"""

    def __init__(self, name: str, description: str, price: float, qty: int,
                 country: str, germ_period: int, color: str):

        super().__init__(name, description, price, qty)
        self.country = country
        self.germ_period = germ_period
        self.color = color



######################

