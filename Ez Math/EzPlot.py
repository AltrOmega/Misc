import matplotlib.pyplot as plt
import numpy as np
from typing import Callable

def plot_func(f: Callable, p: np.linspace,
              x_label = 'x', y_label = 'y', title = 'y = f(x)'):
    x = p
    y = f(p)
    plt.plot(x,y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    

if __name__ == '__main__':
    y = 10
    x_ = 0
    #p = np.linspace(x_-y, x_+y, 400000)
    p = np.linspace(-5, 2.5, 400000)
    f = lambda x: -4*x**3 -12*x**2+16*x
    plot_func(f=f, p=p)

    plt.show()