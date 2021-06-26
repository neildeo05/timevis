import csv
import math
import pandas as pd
import os
import streamlit as st

def query_range(l, h):
    # assert size >= (h-l)
    # level = 23 - round((size / (h-l)) / 1000)
    level = round(math.log((h-l), 2)) - 11
    if level < 0:
        level = 0
    with open("./data/level_%02d.csv" % level, 'r') as r:
        reader = csv.reader(r, delimiter=',')
        return list(filter(lambda x: (x < h and x > l), list(map(int, list(reader)[0]))))


if __name__ == "__main__":
    minv = int(st.slider("Minimum Value for Zoom", 0, 29_000_000))
    maxv = int(st.slider("Maximum Value for Zoom", 1024, 29_000_000))
    a = query_range(minv, maxv)
    df = pd.DataFrame({"data": a})
    st.line_chart(df)
