# _*_ coding = utf-8 _*_
"""
将生成数据的方法整理成一个类
通过初始化定义出的一些变量使得组成一个灵活的生成器
"""

import pandas as pd
import random


class AccountGenerator:
    legal_type = ['char', 'num']

    def __init__(self, seed_num='1234567890', seed_char='qwertyuiopasdfghjklzxcvbnm'):
        self.seed_num = seed_num
        self.seed_char = seed_char

    def generate_account(self, quantity, length, account_structure=[], prefix='', suffix=''):
        account = []
        if len(account_structure) == 0:
            structure_df = pd.DataFrame()
            structure_df['type'] = ['num']
            structure_df['num'] = [length]
        else:
            structure_df = pd.DataFrame(account_structure)
        sum_res = structure_df['num'].sum()
        type_res = set(structure_df['type'].unique())
        flag1 = 0
        if sum_res != length:
            flag1 = -1
        if type_res.issubset(set(self.legal_type)):
            flag2 = 0
        else:
            flag2 = -1
        if flag1+flag2 == 0:
            len_acc = len(prefix) + len(suffix) + length
            item_type = structure_df['type'].values.tolist()
            item_len = structure_df['num'].values.tolist()
            items_num = structure_df.shape[0]
            acc_mod = prefix
            for index, item in enumerate(item_type):
                if item == 'char':
                    acc_mod = acc_mod + self.seed_char[0]*item_len[index]
                else:
                    acc_mod = acc_mod + self.seed_num[0]*item_len[index]

            acc_mod = acc_mod + suffix
            for i in range(quantity):
                acc = prefix
                for index in range(items_num):
                    if item_type[index] == 'char':
                        for j in range(item_len[index]):
                            acc = acc + random.choice(self.seed_char)
                    else:
                        for j in range(item_len[index]):
                            acc = acc + random.choice(self.seed_num)
                acc = acc + suffix
                account.append(acc)
            quantity_final = len(list(set(account)))
            account = sorted(account)
            print('计划生成{}个ID,最终生成不重复ID数:{}\n每个账户号随机生成部分长度为{},生成规则设计为{}\n前缀长度为{}，后缀长度为{},ID最终长度为{},，最终ID样式为{}\n'
                  .format(quantity, quantity_final, length, str(account_structure), len(prefix), len(suffix), len_acc,
                          acc_mod))
            return account
        else:
            if flag1 == -1:
                print('ID生成规则与ID长度矛盾：ID生成规则设计位数{}不等于设置长度{}'.format(sum_res, length))
            if flag2 == -1:
                print('设置格式类型不被识别，合法的数值类型是\'char\',\'num\'')
            return None


if __name__ == '__main__':
    acc_generate = AccountGenerator(seed_num='1234567', seed_char='abcd')
    # res = acc_generate.generate_account(1000, 10, [{'type': 'char', 'num': 3}, {'type': 'num', 'num': 7}], prefix='A',
    #                                     suffix='Z')
    res1 = acc_generate.generate_account(acc_generate, 1000, 10, prefix='A', suffix='Z')
    print(res1)
