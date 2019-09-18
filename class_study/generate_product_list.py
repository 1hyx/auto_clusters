# _*_coding = utf-8 _*_
"""
用于生成关于商品的条目信息
主要关于：商品编号，商品标价
商品标价设计策略也是组合{'尾数':0,'frac':0.2},{0.2,0.05},{0.3,0.05},{0.4,0.05},{0.5,0.2},{0.6,0.05},{0.7,0.05},{0.8,0.05},{0.9,0.15},{0.99,0.15}
"""
import numpy as np


class ProductPrice:
    mantissa_list_default = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99]
    ratio_list_default = [0.2, 0.02, 0.03, 0.02, 0.03, 0.2, 0.1, 0.05, 0.05, 0.15, 0.15]

    def price_list(self, quantity, max_price, min_price, mantissa_list=[], ratio_list=[]):
        mantissa = []
        if len(mantissa_list) == 0:
            for index, man in enumerate(self.mantissa_list_default):
                if index != len(self.mantissa_list_default)-1:
                    mantissa = mantissa + [man for _ in range(int(self.ratio_list_default[index]*quantity))]
                else:
                    mantissa = mantissa + [man for _ in range(quantity - len(mantissa))]
        else:
            for index, man in mantissa_list:
                if index != len(mantissa_list)-1:
                    mantissa = mantissa + [man for _ in range(int(ratio_list[index])*quantity)]
                else:
                    mantissa = mantissa + [man for _ in range(quantity - len(mantissa))]
        int_part = [np.random.randint(low=min_price, high=max_price) for _ in range(quantity)]
        price_list = list(map(lambda x, y: x+y, int_part, mantissa))
        price_list = sorted(price_list)
        return price_list


if __name__ == '__main__':
    product_price = ProductPrice()
    res = product_price.price_list(100, 30, 5)
    print(res)