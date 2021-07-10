import csv
import math
import pandas as pd
import os
import streamlit as st
import sys

def query_range(l, h):
    # Formula is -> log_2 of length(data) minus level value 11
    level = round(math.log((h-l), 2)) - 11
    if level < 0:
        level = 0
    with open("./data/level_%02d.csv" % level, 'r') as r:
        reader = csv.reader(r, delimiter=',')
        data = list(map(int, list(reader)[0]))
        tmp = []
        for idx, i in enumerate(data):
            if(idx > 1023):
                break
            tmp.append(i)
        return tmp

    
def main():
    l = int(sys.argv[-1])
    center_rad = st.checkbox("Display Center/Radius")

    if center_rad:
        a = query_range(0, l)
        center = int(st.slider("Center", 0, len(a), 0))
        radius = int(st.slider("Radius", 0, len(a), 0))
        if (radius == 0):
            df = pd.DataFrame({"data": a})
            st.line_chart(df)
        else:
            assert (center - radius >= 0) or (center + radius <= len(a))
            a = a[center - radius : center + radius]
            df = pd.DataFrame({"data": a})
            st.line_chart(df)
    else:
        minv = int(st.slider("Minimum Value for Zoom", 0,l,0))
        maxv = int(st.slider("Maximum Value for Zoom", 1500, l, l))
        a = query_range(minv, maxv)
        df = pd.DataFrame({"data": a})
        st.line_chart(df)

if __name__ == "__main__":
    main()
