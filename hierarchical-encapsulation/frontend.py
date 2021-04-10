import random

import matplotlib.pyplot as plt
import numpy as np

import backend

NUM_VALS = 2_000


def graph_with_backend():
    data = []
    for i in range(NUM_VALS):
        data.append((random.random() * NUM_VALS - 1) + 1)
    print("There are " + str(backend.num_bars(len(data))) + " bars to choose from")
    msg = "The bar number decides how much data is plotted. The lower the bar number is, the more data will be plotted "
    data = backend.query_select_data(data, input(msg))
    min_data = (backend.decompress_node_array(
        data, backend.Decompress_Arg.MIN))
    max_data = (backend.decompress_node_array(
        data, backend.Decompress_Arg.MAX))
    all_data = (backend.decompress_node_array(
        data, backend.Decompress_Arg.ALL))
    fig, axs = plt.subplots(2)
    axs[0].plot(min_data)
    axs[1].plot(max_data)
    plt.show()


if __name__ == '__main__':
    graph_with_backend()
