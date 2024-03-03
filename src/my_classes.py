from abc import ABC, abstractmethod


class MixinRepr:

    def __init__(self):
        print(f"Создан объект: {repr(self)}")

    def __repr__(self):
        # Product children has incorrect order of values (> 4 attrs)
        # Product has 4 attrs
        # Category has 3 attrs
        # CategoryIter has 1 attr

        values_list = list(self.__dict__.values())
        values_list_correct = values_list[-4:] + values_list[:-4]

        attrs_text = ''
        for value in values_list_correct:
            attrs_text += f"{repr(value)}, "

        return f"{self.__class__.__name__}({attrs_text[:-2]})"


class AbcProduct(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(MixinRepr, AbcProduct):

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

        super().__init__()

    def __repr__(self):
        return super().__repr__()
        #return f'/Product:{self.name},{self.qty}pcs/'

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


class Smartphone(Product):
    """class Smartphone is child of class Product"""

    def __init__(self, name: str, description: str, price: float, qty: int,
                 freq: float, model: str, ram: int, color: str):

        self.freq = freq
        self.model = model
        self.ram = ram
        self.color = color
        super().__init__(name, description, price, qty)


class GreenGrass(Product):
    """class GreenGrass is child of class Category"""

    def __init__(self, name: str, description: str, price: float, qty: int,
                 country: str, germ_period: int, color: str):

        self.country = country
        self.germ_period = germ_period
        self.color = color
        super().__init__(name, description, price, qty)

###############################


class AbcCategoryOrder(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Category(MixinRepr, AbcCategoryOrder):

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
        self.record_product_name()
        super().__init__()

    def record_product_name(self):
        for good in self.__goods:
            Category.unique_product_names.add(good.get_name())

        Category.number_of_products_types = len(Category.unique_product_names)

    def add_product_in_category(self, product):
        if not isinstance(product, Product):
            raise TypeError('Добавить в категорию можно только продукт или его наследников')

        self.__goods.append(product)

    def __repr__(self):
        return super().__repr__()
        #return f'*Category:{self.name}*\n*Contains:{self.__goods}*\n'

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


class CategoryIter(MixinRepr):

    def __init__(self, category):
        """

        :param category: объект класса Category

        :attr goods: список товаров в строковом виде (можно изменить если будет нужно)
        """
        self.goods = category.list_of_goods
        super().__init__()

    def __repr__(self):
        return super().__repr__()

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


class Order(MixinRepr, AbcCategoryOrder):
    """
    ordered Product
    ordered qty
    ordered total price
    """

    def __init__(self, product: Product, order_qty, order_price):
        self.product = product
        self.order_qty = order_qty
        self.order_price = order_price
        super().__init__()

    def __repr__(self):
        return super().__repr__()

    def __str__(self):
        return f'В заказе: /{self.product}/, {self.order_qty} шт.'


######################
