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


class Product:

    def __init__(self, name="", description="", price=0.0, qty=0):

        self.name = name
        self.description = description
        self.__price = price
        self.qty = qty

    def __repr__(self):
        return f'/Product:{self.name},{self.qty}pcs/'

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.qty} шт.'

    def __add__(self, other):

        return self.price * self.qty + other.price * other.qty


    def get_name(self):
        return self.name

    @classmethod
    def new_product(cls, name, description, price, quantity, product_list=None):

        # если получили список, ищем совпадающий продукт
        if product_list:
            # ищем совпадающий продукт по имени
            for product in product_list:
                if product.name == name:
                    # если нашли, складываем количество
                    # если нашли, выбираем наибольшую цену
                    product.qty += quantity
                    if product.price < price:
                        product.price = price

                    # возвращаем обновлённый продукт
                    return product

            # если не нашли совпадающий продукт:
        # если не получили список и не искали:

        # возвращаем новый продукт
        return cls(name, description, price, quantity)

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

######################
