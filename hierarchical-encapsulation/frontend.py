import random

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

import backend

NUM_VALS = 20_000


def graph_with_backend():
    data = []
    n, p = 10, 0.5
    raw_data = binom.rvs(n, p, size=NUM_VALS)
    print("There are " + str(backend.num_bars(len(raw_data))) +
          " bars to choose from")
    msg = "The bar number decides how much data is plotted. The lower the bar number is, the more data will be plotted. The top plot is the min data, and the bottom plot is the max data "
    data = backend.query_select_data(raw_data, input(msg))
    min_data = (backend.decompress_node_array(
        data, backend.Decompress_Arg.MIN))
    max_data = (backend.decompress_node_array(
        data, backend.Decompress_Arg.MAX))
    all_data = (backend.decompress_node_array(
        data, backend.Decompress_Arg.ALL))
    fig, axs = plt.subplots(3)
    axs[0].plot(min_data)
    axs[1].plot(max_data)
    axs[2].plot(raw_data)
    plt.show()


if __name__ == '__main__':
    graph_with_backend()
