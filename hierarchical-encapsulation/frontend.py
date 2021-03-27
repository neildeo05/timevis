import matplotlib.pyplot as plt
import numpy as np
import random
import backend
NUM_VALS=2_000_000

def graph_with_backend():
  data = []
  for i in range(NUM_VALS):
      data.append((random.random() * NUM_VALS - 1) + 1)
  print("There are " + str(backend.num_bars(len(data))) + " bars to choose from")
  msg = "The bar number decides how much data is plotted. The lower the bar number is, the more data will be plotted "
  data = backend.query_select_data(data, input(msg))
  data = np.array(data)
  max_data = np.array(backend.filter_data(data, backend.Decompress_Arg.MAX))
  min_data = np.array(backend.filter_data(data, backend.Decompress_Arg.MIN))
  all_data = np.array(backend.filter_data(data, backend.Decompress_Arg.ALL))
  fig, axs = plt.subplots(3)
  axs[0].plot(max_data[:,0], max_data[:,1])
  axs[1].plot(min_data[:,0], min_data[:,1])
  axs[2].plot(all_data[:,0], all_data[:,1])

  plt.show()


if __name__ == '__main__':
    graph_with_backend()
