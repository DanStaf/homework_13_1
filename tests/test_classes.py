from src.my_classes import Category
from src.my_classes import CategoryIter
from src.my_classes import Product
import pytest
import mock
import builtins

banana_10 = Product('banana', 'fruits', 100.99, 10)
apple_15 = Product('apple', 'fruits', 51.99, 15)
apple_150 = Product('apple', 'fruits', 51.99, 150)

fruits = Category('fruits', 'food', [banana_10, apple_15])
fruits.add_product_in_category(apple_150)

apples = Category('apples', 'fruits', [apple_15, apple_150])


def test_classes():

    bread_0 = Product('bread', 'fresh bread hand made today', 25, 0)
    assert bread_0.name == 'bread'

    assert Product('bread', 'fresh bread hand made today', 25, 2).qty == 2


def test_product():

    assert banana_10.name == 'banana'
    assert banana_10.description == 'fruits'
    assert banana_10.price == 100.99
    assert banana_10.qty == 10


def test_category():

    assert fruits.name == 'fruits'
    assert fruits.description == 'food'
    #assert fruits.goods == [banana_10, apple_15, apple_150]


def test_number_of_categories():

    assert fruits.number_of_categories == 2
    assert apples.number_of_categories == 2
    assert Category.number_of_categories == 2


def test_number_of_products_types():

    assert fruits.number_of_products_types == 2
    assert apples.number_of_products_types == 2
    assert Category.number_of_products_types == 2

def test_list_of_goods():
    assert fruits.list_of_goods == ['banana, 100.99 руб. Остаток: 10 шт.',
                                    'apple, 51.99 руб. Остаток: 15 шт.',
                                    'apple, 51.99 руб. Остаток: 150 шт.']

    assert apples.list_of_goods == ['apple, 51.99 руб. Остаток: 15 шт.',
                                    'apple, 51.99 руб. Остаток: 150 шт.']


def test_new_product():

    a1 = Product.new_product('apple', 'fruits', 14.99, 3)
    a2 = Product('apple', 'fruits', 14.99, 3)
    assert a1.name == a2.name
    assert a1.qty == a2.qty


def test_new_product_with_list():
    p1 = Product.new_product('apple', 'fruits', 14.99, 3)
    p2 = Product('orange', 'fruits', 20.99, 3)
    p_list = [p1, p2]
    p3 = Product.new_product('apple', 'fruits', 100.0, 3, p_list)

    assert p3.name == 'apple'
    assert p3.price == 100.0
    assert p3.qty == 6


def test_price_get_set_del():

    # banana_10.price == 100.99

    del banana_10.price
    assert banana_10.price is None

    banana_10.price = 102
    assert banana_10.price == 102

    banana_10.price = -1111
    assert banana_10.price == 102


def test_price_with_input():

    with mock.patch.object(builtins, 'input', lambda _: 'n'):
        banana_10.price = 50
        assert banana_10.price != 50

    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        banana_10.price = 50
        assert banana_10.price == 50


def test_str():

    assert str(apple_15) == 'apple, 51.99 руб. Остаток: 15 шт.'
    assert str(apples) == 'apples, количество продуктов: 165 шт.'


def test_len_category():

    assert len(apples) == 165


def test_add_for_products():
    p1 = Product.new_product('apple', 'fruits', 14.99, 3)
    p2 = Product('orange', 'fruits', 20.99, 3)
    assert p1 + p2 == 107.94


def test_iter():

    my_iter = CategoryIter(apples)

    assert len(my_iter) == 2

    assert [str(each_good) for each_good in my_iter] == ['apple, 51.99 руб. Остаток: 15 шт.',
                                                         'apple, 51.99 руб. Остаток: 150 шт.']

