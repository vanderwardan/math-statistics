import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
from statsmodels.nonparametric.kde import KDEUnivariate

coin = sps.bernoulli(0.5).rvs  # симметричная монета
# coin(size=10) --- реализация 10 бросков монеты

def uniform(size=100, precision=30):
    a = np.exp2(np.arange(-1, -precision-1, -1))
    b = coin(precision * np.prod(size)).reshape(precision, np.prod(size))
    return (a @ b).reshape(size)

def normal(size=1, loc=0, scale=1, precision=30):
    ksi = uniform(size, precision)
    etta = uniform(size, precision)
    return np.cos(2*np.pi*ksi) * np.sqrt(-2*np.log(etta)) * scale + loc

def expon(size=1, lambd=1, precision=30):
    return -1/lambd * np.log(uniform(size, precision))


def draw_ecdf(sample, grid, cdf=None):
    ''' По сетке grid cтроит графики эмпирической функции распределения
    и истинной (если она задана) для всей выборки и для 1/10 ее части.
    '''

    plt.figure(figsize=(16, 3))
    for i, size in enumerate([len(sample) // 10, len(sample)]):
        plt.subplot(1, 2, i + 1)

        plt.scatter(sample[:size], np.zeros_like(sample[:size]),
                    alpha=0.4, label='sample')

        if cdf is not None:
            plt.plot(grid,
                     cdf(grid),
                     color='green', alpha=0.3, lw=2, label='true cdf')

        plt.plot(grid,
                 ECDF(sample[:size])(grid),
                 color='red', label='ecdf')

        plt.legend()
        plt.grid(ls=':')
        plt.title('sample size = {}'.format(size))
    plt.show()