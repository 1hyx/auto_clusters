# __*__ coding = utf-8 __*__

"""
用于生成关于商品的条目信息
主要关于：商品编号，商品标价
商品标价设计策略也是组合{'尾数':0,'frac':0.2},{0.2,0.05},{0.3,0.05},{0.4,0.05},{0.5,0.2},{0.6,0.05},{0.7,0.05},{0.8,0.05},{0.9,0.15},{0.99,0.15}
"""
import numpy as np


class ProductPrice:
    mantissa_list_default = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99]
    ratio_list_default = [0.2, 0.02, 0.03, 0.02, 0.03, 0.2, 0.1, 0.05, 0.05, 0.15, 0.15]
    unit_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    unit_ratio_list = [0.24, 0.01, 0.01, 0.01, 0.01, 0.3, 0.01, 0.01, 0.15, 0.25]

    def price_list(self, quantity, max_price, min_price, mantissa_list=[], ratio_list=[]):
        mantissa = []
        units = []
        time_of_X = max(int(np.math.log(max_price, 10)), 1)
        if len(mantissa_list) == 0:
            mantissa_list = self.mantissa_list_default
            ratio_list = self.ratio_list_default
        unit_list = self.unit_list
        unit_ratio_list = self.unit_ratio_list
        if time_of_X >= 3:
            int_part = [int(np.random.randint(low=max(10, min_price), high=max_price)/10)*10 for _ in range(quantity)]
            for index, man in enumerate(mantissa_list):
                if index != len(mantissa_list)-1:
                    mantissa = mantissa + [man for _ in range(int(ratio_list[index]*quantity))]
                    units = units + [unit_list[index] for _ in range(int(unit_ratio_list[index]*quantity))]
                else:
                    mantissa = mantissa + [man for _ in range(quantity - len(mantissa))]
                    units = units + [unit_list[index] for _ in range(quantity - len(units))]
            mantissa = map(lambda x, y: x+y, units, mantissa)
        else:
            int_part = [np.random.randint(low=min_price, high=max_price)for _ in range(quantity)]
            for index, man in enumerate(mantissa_list):
                if index != len(mantissa_list) - 1:
                    mantissa = mantissa + [man for _ in range(int(ratio_list[index] * quantity))]
                else:
                    mantissa = mantissa + [man for _ in range(quantity - len(mantissa))]
        price_list = list(map(lambda x, y: x+y, int_part, mantissa))
        price_list = sorted(price_list)
        return price_list


if __name__ == '__main__':
    product_price = ProductPrice()
    res = product_price.price_list(100, 1000, 10)
    print(res)
