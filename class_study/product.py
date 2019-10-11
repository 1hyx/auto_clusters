
import pandas as pd

# 生成的accounts 和 价格构成了 完整的产品信息表
from class_study.generate_account import AccountGenerator
from class_study.generate_product_list import ProductPrice


class ProductList:
    id_length = 10
    id_structure = []
    id_prefix = ''
    id_suffix = ''

    def __init__(self, quantity):
        self.quantity = quantity

    """
    set_id 函数可以保证生成ID的格式
    length 自定义部分长度
    structure [{'type':'char','num':4},{'type':'num', 'num':4}] 要求设置的随机生成部分的结构
    prefix 前缀
    suffix 后缀
    """
    def set_id(self, length, structure=[], prefix='', suffix=''):
        self.id_length = length
        self.id_structure = structure
        self.id_prefix = prefix
        self.id_suffix = suffix

    min_price = 3
    max_price = min_price+500

    """
    set_price 函数保证设计的价格的最大值和最小值
    min_price: 最低价格
    max_price: 最高价格
    """
    def set_price(self, max_price, min_price):
        self.max_price = max_price
        self.min_price = min_price

    """
    最终获得商品价格编号列表的函数
    """
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
