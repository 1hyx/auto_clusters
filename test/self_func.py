import numpy as np
import math
from matplotlib import pyplot as plt


def plot_func(func_type, func):
    x = np.arange(-10, 10, 0.05)
    mu = func[0]
    sig = func[1]
    np.random.normal()
    def normal_func(xi):
        yi = math.exp(-(xi - mu) ** 2 / (2 * sig ** 2)) / ((2 * math.pi) ** 0.5 * sig)
        return yi

    if func_type == 'normal':
        y = list(map(normal_func, x))
        plt.title("the plot of Y~N({},{})".format(mu, sig))
        plt.plot(x, y)
        plt.show()
    return 0


# func_list:一系列分布的参数：例如[{'type':'normal','args':['mu':0,'sigma':1]},{'type':'normal','args':['mu':0,'sigma':1]}]
def generate_composite_distribution(func_list):
    x = np.arange(-10, 10, 0.05)
    z = x.shape
    y = np.zeros(z)
    for fun in func_list:
        if fun['type'] == 'normal':
            mu = fun['args']['mu']
            sig = fun['args']['sigma']
            def normal_func(xi):
                yi = math.exp(-(xi - mu) ** 2 / (2 * sig ** 2)) / ((2 * math.pi) ** 0.5 * sig)
                return yi
            y = y + list(map(normal_func, x))
    plt.plot(x, y)
    plt.title("the plot for Y~N({},{})+N({},{})")
    plt.show()




if __name__ == '__main__':
    plot_func('normal', [0, 2])
    generate_composite_distribution([{'type': 'normal', 'args': {'mu': 0, 'sigma': 1}},
                                     {'type': 'normal', 'args': {'mu': 3, 'sigma': 1}}])
