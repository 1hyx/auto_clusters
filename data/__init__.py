# _*_ coding:utf-8 _*_
# __author__ = 'huyuxin'
"""
随机生成消费记录
Randomly generate expenses record according to rules
包含字段 linkages
账户号 消费时间  消费金额 消费类型
account，consumption time, amount of consumption, type of consumption
时间跨度： 2016.6.30-2019.8.31
消费时间：在工作日符合三个时段的正态分布综合，在非工作日符合另外三个正态分布的综合
the time of consumption: on week days, the distribution is the combination of three independent normal distributions;
on weekend, another three.
消费金额：分为大额和小额 ，金额呈现厚尾正态分布
the amount of consumption: large and small, the distribution will be Thick tail normal distribution
消费类型：分为分期、退款、消费
type of consumption:  staging, refund, consumption, staging and refund happen as a normal distribution with low average
"""

import pandas as pd
from random import choice
seed = '1234567890'


def generate_account(n, num_len):
    name_list = []
    for i in range(n):
        name = ''
        for j in range(num_len):
            name = name+choice(seed)
        name_list.append(name)
    return name_list


# def generate_data(total):





if __name__ == '__main__':
    x = generate_account(100, 8)
    print(x)

