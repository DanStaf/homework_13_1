import my_classes
import json


def get_classes_from_file():
    """
    функция читает файл products.json и создаёт объекты классов.

    :return: list of classes Category
    """

    with open("../products.json", 'r', encoding='utf-8') as f:
        reading_result = json.loads(f.read())

    categories = []

    for each_result in reading_result:
        if each_result:
            goods = []
            for each_product in each_result['products']:
                if each_product:
                    new_product = my_classes.Product(each_product['name'],
                                                     each_product['description'],
                                                     each_product['price'],
                                                     each_product['quantity'])
                    goods.append(new_product)

            new_category = my_classes.Category(each_result['name'],
                                               each_result['description'],
                                               goods)

            categories.append(new_category)

    return categories


check = get_classes_from_file()
[print(item) for item in check]

print("number_of_categories:", my_classes.Category.number_of_categories)
print("number_of_products_types:", my_classes.Category.number_of_products_types)
print("unique_product_names:", my_classes.Category.unique_product_names)
