import random

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

import backend
import pandas as pd

# NUM_VALS = 29_000_000
BOX_SIZE = 1024


def graph_with_backend():
    import streamlit as st
    
    # Raw data can either be linear, which is first line of code, or it can be the sine curve
    # raw_data = list(range(0, NUM_VALS)) 
    import csv
    with open('top100k.csv', newline='') as f:
        reader = csv.reader(f, delimiter='\n')
        t = list(reader)
        raw_data = [int(i[0]) for i in t]


    minv = st.slider("Minimum Value for Zoom", 0, len(raw_data)) 
    maxv = st.slider("Maximum Value for Zoom", 0, len(raw_data))
    assert(minv <= maxv);
    # min_v = st.text_input('Minimum Value for Zoom')
    # max_v = st.text_input('Maximum Value for Zoom')
    min_v = minv
    max_v = maxv
    if min_v and max_v:
        min_v = int(min_v)
        max_v = int(max_v)
        data = backend.query_select_data_range(min_v, max_v, raw_data, False)
        all_data = (backend.decompress_node_array(
            data, backend.Decompress_Arg.ALL))
        df = pd.DataFrame({"data": all_data[:,1]})
        st.line_chart(df)


if __name__ == '__main__':
    graph_with_backend()
