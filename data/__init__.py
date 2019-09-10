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
import random
import pandas as pd

seed = '0123456789'


def accounts_list_with_differ_num(accounts, person_num, person_money):
    df_person_num = pd.DataFrame(data=person_num, columns=['num'])
    df_accounts = pd.DataFrame(data=accounts, columns=['name'])
    df_person_money = pd.DataFrame(data=person_money, columns=['money'])
    accounts_in_use = df_accounts[df_person_num['num'] > 0].values.tolist()
    person_num_in_use = df_person_num[df_person_num['num'] > 0].values.tolist()
    person_money_in_use = df_person_money[df_person_num['num'] > 0].values.tolist()
    name_list = []
    money_list = []
    for i, per_num in enumerate(person_num_in_use):
        temp_list = [accounts_in_use[i][0] for j in range(per_num[0])]
        name_list = name_list+temp_list
        temp_money_list = []
        for k in range(per_num[0]):
            if k % 5 != 0:
                temp_money_list.append(round(person_money_in_use[i][0]/per_num[0], 2) + int(random.choice(seed))*10)
            else:
                temp_money_list.append(round(person_money_in_use[i][0]/(per_num[0]*2), 2))
        money_list = money_list + temp_money_list
    return name_list, money_list



