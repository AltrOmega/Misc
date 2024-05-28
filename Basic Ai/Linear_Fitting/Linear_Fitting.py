import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, List

def double_plot_fig(f_1: Callable, f_2: Callable, x: List[float]) -> plt:
    fig, ax = plt.subplots()
    ax.plot(x, f_1(x), label="Original")
    ax.plot(x, f_2(x), color='yellow', label="Adjusted")
    ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5, color='#BDBDBD')
    ax.grid(True, which='both', axis='x', linestyle='--', linewidth=0.5, color='#616161')
    ax.legend()
    return fig

def linear(w, x, b):
    return w * x + b

x_points = np.linspace(-10, 10, 100)
y_points = linear(1, x_points, 1)
linLambda = lambda x: linear(1, x, 1)

def calculate_loss(f, linespace, expected):
    total_loss = 0
    for i in range(len(linespace)):
        x = linespace[i]
        y = expected[i]
        total_loss += abs(abs(f(x)) - abs(y))
    return total_loss

def index_of_smallest(values):
    if not values:
        raise ValueError("The list is empty")
    smallest_index = 0
    smallest_value = values[0]
    for i in range(1, len(values)):
        if values[i] < smallest_value:
            smallest_value = values[i]
            smallest_index = i
    return smallest_index

def nudge_f(w, b, nudge):
    changedFunc = lambda x: linear(w, x, b)
    loss_origin = calculate_loss(changedFunc, x_points, y_points)

    changedFunc = lambda x: linear(w + nudge, x, b)
    loss_w_plus = calculate_loss(changedFunc, x_points, y_points)

    changedFunc = lambda x: linear(w - nudge, x, b)
    loss_w_minus = calculate_loss(changedFunc, x_points, y_points)

    changedFunc = lambda x: linear(w, x, b + nudge)
    loss_b_plus = calculate_loss(changedFunc, x_points, y_points)

    changedFunc = lambda x: linear(w, x, b - nudge)
    loss_b_minus = calculate_loss(changedFunc, x_points, y_points)

    i = index_of_smallest([loss_origin, loss_w_plus, loss_w_minus, loss_b_plus, loss_b_minus])

    if i == 0:
        return w, b
    if i == 1:
        return w + nudge, b
    if i == 2:
        return w - nudge, b
    if i == 3:
        return w, b + nudge
    if i == 4:
        return w, b - nudge

w = 0
b = 0
epoch =  41
nudge = 0.05
snapshots = []
for i in range(epoch):
    if i % 10 == 0:
        snapshots.append((w, b))
    w, b = nudge_f(w, b, nudge)

fig, axs = plt.subplots(1, 5, figsize=(25, 5))
for i, ax in enumerate(axs.flat):
    if i < len(snapshots):
        w, b = snapshots[i]
        ax.plot(x_points, linLambda(x_points), label="Original")
        ax.plot(x_points, linear(w, x_points, b), color='yellow', label=f"Epoch {i*10}")
        ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5, color='#BDBDBD')
        ax.grid(True, which='both', axis='x', linestyle='--', linewidth=0.5, color='#616161')
        ax.legend()

plt.subplots_adjust(wspace=0.4)
plt.tight_layout()
plt.show()
