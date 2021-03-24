import matplotlib.pyplot as plt
import numpy as np
import random
import backend
NUM_VALS=1000000
def graph_with_backend():
  data = []
  for i in range(NUM_VALS):
      data.append((random.random() * NUM_VALS - 1) + 1)
  print("There are " + str(backend.num_bars(len(data))) + " bars to choose from")
  msg = "The larger the bar is, the finer the resulting data is. For example, in a scenario where there are 5 bars, bar 5 would contain the most amount of data, and bar 0 would contain the least amount of data: "
  max_data = backend.query_select_data(data, input(msg))
  min_data = backend.query_select_data(data, input(msg))
  max_data = np.array(backend.filter_data(max_data, backend.Decompress_Arg.MAX))
  min_data = np.array(backend.filter_data(min_data, backend.Decompress_Arg.MIN))
  fig, axs = plt.subplots(2)
  axs[0].plot(max_data[:,0], max_data[:,1])
  axs[1].plot(min_data[:,0], min_data[:,1])

  # plt.plot(max_data[:,0], max_data[:,1])
  plt.show()
  # all_data = np.array(backend.query_select_data(data, backend.Decompress_Arg.ALL, input(msg)))


if __name__ == '__main__':
    graph_with_backend()
