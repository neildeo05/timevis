import random

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

import backend
import pandas as pd

NUM_VALS = 29_000_000
BOX_SIZE = 1024


def graph_with_backend():
    import streamlit as st

    min_v = st.text_input('Minimum Value for Zoom')
    max_v = st.text_input('Maximum Value for Zoom')
    if min_v and max_v:
        raw_data = list(range(0, NUM_VALS))
        min_v = int(min_v)
        max_v = int(max_v)
        data = backend.query_select_data_range(min_v, max_v, raw_data, False)
        all_data = (backend.decompress_node_array(
            data, backend.Decompress_Arg.ALL))
        df = pd.DataFrame({"data": all_data[:,1]})
        st.line_chart(df)


if __name__ == '__main__':
    graph_with_backend()
