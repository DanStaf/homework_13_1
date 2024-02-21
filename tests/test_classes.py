from src.my_classes import Category
from src.my_classes import Product
import pytest

banana_10 = Product('banana', 'fruits', 100.99, 10)
apple_15 = Product('apple', 'fruits', 51.99, 15)
apple_10 = Product('apple', 'fruits', 51.99, 150)

fruits = Category('fruits', 'food', [banana_10, apple_15])
fruits.add_product_in_category(apple_10)

apples = Category('apples', 'fruits', [apple_15, apple_10])


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
    #assert fruits.goods == [banana_10, apple_15, apple_10]


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

    p1 = Product.new_product('apple', 'fruits', 14.99, 3)
    p2 = Product('apple', 'fruits', 14.99, 3)
    assert p1.name == p2.name
    assert p1.qty == p2.qty


def test_new_product_with_list():

    p1 = Product.new_product('apple', 'fruits', 14.99, 3)
    p2 = Product('orange', 'fruits', 20.99, 3)

    p_list = [p1, p2]
    p3 = Product.new_product('apple', 'fruits', 100.0, 3, p_list)

    assert p3.name == 'apple'
    assert p3.price == 100.0
    assert p3.qty == 6

