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

