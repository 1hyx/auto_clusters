
import pandas as pd

from class_study.generate_account import AccountGenerator
from class_study.generate_product_list import ProductPrice


class ProductList:
    id_length = 10
    id_structure = []
    id_prefix = ''
    id_suffix = ''

    def __init__(self, quantity):
        self.quantity = quantity

    def set_id(self, length, structure=[], prefix='', suffix=''):
        self.id_length = length
        self.id_structure = structure
        self.id_prefix = prefix
        self.id_suffix = suffix

    max_price = 500
    min_price = 3

    def set_price(self, max_price, min_price):
        self.max_price = max_price
        self.min_price = min_price

    def get_product_list(self):
        acc_generator = AccountGenerator()
        acc = acc_generator.generate_account(quantity=self.quantity, length=self.id_length, prefix=self.id_prefix,
                                       suffix=self.id_suffix, account_structure=self.id_structure)
        price_generator = ProductPrice()
        price = price_generator.price_list(quantity=self.quantity, max_price=self.max_price, min_price=self.min_price)
        product = pd.DataFrame(columns=['ID', 'PRICE'])
        product['ID'] = acc
        product['PRICE'] = price
        return product


if __name__ == '__main__':
    data = ProductList(quantity=1000)
    data.set_id(length=10, prefix='ID', suffix='new')
    data.set_price(max_price=10000, min_price=20)
    res = data.get_product_list()
