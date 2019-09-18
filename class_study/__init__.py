# _*_coding=utf-8 _*_
# 学习基于python 的面向对象编程，果然function太多了就是要用class，在我目前的认识里这是最好的标记方法属于谁给谁用的方式
# 放了一个最简单的例子


class MyClass:
    feature = [1, 2, 3, 4, 5]
    data = []

    # 每实例化一次会自动调用__init__
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        return self


if __name__ == '__main__':
    x = MyClass('sad')
    print(x.name)
    print(x.feature)
    x.feature = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(x.feature)



