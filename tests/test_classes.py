from src.my_classes import Category
from src.my_classes import CategoryIter
from src.my_classes import Product
from src.my_classes import Smartphone
from src.my_classes import GreenGrass

import pytest
import mock
import builtins


def test_product():

    bread_2 = Product('bread', 'fresh bread hand made today', 25, 2)
    banana_10 = Product('banana', 'fruits', 100.99, 10)

    assert banana_10.name == 'banana'
    assert banana_10.description == 'fruits'
    assert banana_10.price == 100.99
    assert banana_10.qty == 10

    # test price @property

    # banana_10.price == 100.99

    del banana_10.price
    assert banana_10.price is None

    banana_10.price = 102
    assert banana_10.price == 102

    banana_10.price = -1111
    assert banana_10.price == 102

    with mock.patch.object(builtins, 'input', lambda _: 'n'):
        banana_10.price = 50
        assert banana_10.price != 50

    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        banana_10.price = 50
        assert banana_10.price == 50

    # test methods

    assert str(banana_10) == 'banana, 50 руб. Остаток: 10 шт.'

    assert repr(banana_10) == "Product('banana', 'fruits', 50, 10)"


def test_product_methods__new_add():

    apple_data_1 = {
        "name": "apple",
        "description": "fruits",
        "price": 14.99,
        "qty": 3
    }

    a1 = Product.new_product(**apple_data_1)
    a1_1 = Product(apple_data_1['name'],
                   apple_data_1['description'],
                   apple_data_1['price'],
                   apple_data_1['qty'])

    assert a1.name == a1_1.name
    assert a1.qty == a1_1.qty

    o1 = Product('orange', 'fruits', 20.99, 3)
    product_list = [a1, o1]

    apple_data_2 = {
        "name": "apple",
        "description": "fruits",
        "price": 100.00,
        "qty": 3
    }

    a2 = Product.new_product(product_list, **apple_data_2)

    assert a2.name == 'apple'
    assert a2.price == 100.0
    assert a2.qty == 6

    assert a1_1 + a2 == 14.99 * 3 + 100 * 6


def test_category():

    banana_10 = Product('banana', 'fruits', 100.99, 10)
    apple_15 = Product('apple', 'fruits', 51.99, 15)
    apple_150 = Product('apple', 'fruits', 51.99, 150)

    fruits = Category('fruits', 'food', [banana_10, apple_15])
    fruits.add_product_in_category(apple_150)

    apples = Category('apples', 'fruits', [apple_15, apple_150])

    assert fruits.name == 'fruits'
    assert fruits.description == 'food'

    assert fruits.number_of_categories == 2
    assert apples.number_of_categories == 2
    assert Category.number_of_categories == 2

    assert fruits.number_of_products_types == 2
    assert apples.number_of_products_types == 2
    assert Category.number_of_products_types == 2

    assert fruits.list_of_goods == ['banana, 100.99 руб. Остаток: 10 шт.',
                                    'apple, 51.99 руб. Остаток: 15 шт.',
                                    'apple, 51.99 руб. Остаток: 150 шт.']

    assert apples.list_of_goods == ['apple, 51.99 руб. Остаток: 15 шт.',
                                    'apple, 51.99 руб. Остаток: 150 шт.']

    # test methods

    assert str(apples) == 'apples, количество продуктов: 165 шт.'
    assert len(apples) == 165

    # record_product_name tested above
    # (number_of_products_types depends on this method)

    # add_product_in_category
    # tested above for standard product
    # below for child and type error

    gg = GreenGrass('Газон гном',
                    'Наш газон самый лучший газон',
                    200,
                    50,
                    'Holland',
                    30,
                    'Зелёный')

    fruits.add_product_in_category(gg)
    assert fruits.list_of_goods == ['banana, 100.99 руб. Остаток: 10 шт.',
                                    'apple, 51.99 руб. Остаток: 15 шт.',
                                    'apple, 51.99 руб. Остаток: 150 шт.',
                                    'Газон гном, 200 руб. Остаток: 50 шт.']

    with pytest.raises(TypeError):
        fruits.add_product_in_category(500)

    # test iter

    my_iter = CategoryIter(apples)

    assert len(my_iter) == 2

    assert [str(each_good) for each_good in my_iter] == ['apple, 51.99 руб. Остаток: 15 шт.',
                                                         'apple, 51.99 руб. Остаток: 150 шт.']


def test_child_classes():

    sf = Smartphone('Samsung',
                    '256GB, Серый цвет, 200MP камера',
                    180000.0,
                    5,
                    3.36,
                    'Galaxy C23 Ultra',
                    256,
                    'Серый')

    gg = GreenGrass('Газон гном',
                    'Наш газон самый лучший газон',
                    200,
                    50,
                    'Holland',
                    30,
                    'Зелёный')

    gg2 = GreenGrass('Газон спорт',
                     'Наш газон самый лучший газон',
                     220,
                     50,
                     'Russia',
                     10,
                     'Зелёный')

    assert isinstance(sf, Product)
    assert isinstance(gg, Product)

    assert sf.ram == 256
    assert gg.color == 'Зелёный'

    # test methods

    assert str(sf) == 'Samsung, 180000.0 руб. Остаток: 5 шт.'

    assert gg + gg2 == 220 * 50 + 200 * 50

    with pytest.raises(TypeError):
        assert gg + sf is None

    product_data = {
        "name": "Samsung",
        "description": "phone",
        "price": 100000.00,
        "qty": 3,
        "freq": 3.36,
        "model": 'Galaxy C23 Ultra',
        "ram": 256,
        "color": 'Серый'
    }

    added_product = Smartphone.new_product(**product_data)

    assert added_product.qty == 3
    assert added_product.ram == 256


