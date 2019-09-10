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

生成规则：
账户号不重复
生成消费记录后，按照正态分布分配给不同账户，即有部分账户的消费记录多一些
"""

import pandas as pd
from scipy.stats import norm
import numpy as np
from random import choice
import math
import random
from data import accounts_list_with_differ_num


seed = '1234567890'
year = ['2016', '2017', '2018', '2019']
month = [str(i) for i in range(1, 13, 1)]
day = [31, 30, 31, 28, 31, 30, 31, 31, 30, 31, 30, 31]
hour = [str(h) for h in range(0, 24, 1)]
minute = [str(m) for m in range(0, 60, 1)]
second = [str(s) for s in range(0, 60, 1)]


# 生成账户号
def generate_account(n, num_len):
    if math.log(n, 10) >= num_len/2:
        print('the amount of accounts is too large so that with probability to generate same series! the list will '
              'finally unique. the total num would less than you expect!.')
    name_list = []
    for i in range(n):
        name = ''
        for j in range(num_len):
            name = name+choice(seed)
        name_list.append(name)
    name_list = list(set(name_list))
    print(len(name_list))
    return name_list


# 生成消费发生时间，分布应当符合一些正态分布的综合
# total 一共要多少记录
# distribution_list 使用的分布的说明 type:list(dict)
"""
for example:
distribution_list =['type':'normal','args':['mean':1,'stand_var':1]],['type':'normal','args':['mean':2,'stand_var':2]]
"""


# 生成时间分秒
def generate_minute_second(num):
    times = max(int(num / 60)+1, 1)
    minute_list = random.sample(minute, 60)
    second_list = random.sample(second, 60)
    min_sec = list(map(lambda x, y: x + 'm-'+y+'s', minute_list, second_list))
    min_sec_list = []
    for _ in range(times):
        min_sec_list = min_sec_list + min_sec
    return min_sec_list


# 基础版本
# 假设1 每天的消费总量是一样的 暂时不区分工作日和非工作日
# 假设2 每天的订单发生时间是基于三个正态分布的总和
def generate_hour_time(total):
    x2 = np.zeros([24])
    x1 = np.zeros([24])
    x3 = np.zeros([24])
    x4 = np.zeros([24])
    for i, _ in enumerate(x2):
        x2[i] = norm.cdf(i-11)-norm.cdf(i-12)
    x1[0:20] = x2[4:24]
    x3[5:24] = x2[0:19]
    x4[8:24] = x2[0:16]
    sum_result = (x1+x2+x3+x4)*total/4
    hour_order_num = [int(item) for item in sum_result]
    hour_order_num[0] = max(total - sum(hour_order_num[1:]), 0)
    time_list = []
    for i, item in enumerate(hour_order_num):
        temp_min_sec = generate_minute_second(item)
        if len(temp_min_sec) > 0:
            hour_min_sec = list(map(lambda x: str(i)+'h-'+x, temp_min_sec))
            print(len(hour_order_num))
            time_list = time_list + hour_min_sec
            print(len(time_list))
    return time_list


# 每个人的消费习惯不一样
# 假设1 人群的消费行为是稳定的，同时人群的消费频率分布符合正态分布，均值5，标准差2
def account_record_num(accounts, record_num):
    acc_num = []
    acc_money = []
    times = record_num/len(accounts)
    for acc in accounts:
        num = max(int(np.random.normal(5, 2)*times), 0)
        if num > 5:
            money = 500 + int(choice(seed))*100 - random.random()*10
        else:
            money = 1000 - int(random.choice(seed))*100 + random.random()*10
        acc_num.append(num)
        acc_money.append(money)
    return acc_num, acc_money


# 生成
def generate_record(account_num, account_len, record_num,save_path):
    accounts = generate_account(account_num, account_len)
    person_num, person_money = account_record_num(accounts, record_num)
    account_num_list, account_money_list = accounts_list_with_differ_num(accounts, person_num, person_money)
    accounts_df = pd.DataFrame(data=account_num_list, columns=['account'])
    accounts_df['money'] = account_money_list
    accounts_df = accounts_df.sample(n=record_num, random_state=42)
    accounts_df.index = range(record_num)
    record_time = random.sample(generate_hour_time(record_num), record_num)
    accounts_df['time'] = record_time
    accounts_df.to_csv(save_path, index=None)
    return accounts_df


if __name__ == '__main__':
    record_final = generate_record(10000, 8, 10000, '../generate_data/file2.csv')
    print(record_final)


