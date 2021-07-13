import csv
import math
import pandas as pd
import os
import streamlit as st
import sys
#TODO: Try to use functoools' lru_cache for memoization

g_max_value = 2000

def find_level(l, h):
    global g_max_value
    delta = (h - l) + 1
    count = 1
    while(delta > g_max_value):
        h //= 2
        l //= 2
        delta = (h - l) + 1
        count+=1
    return (count-1, l, h)

def query_range(l, h):
    level, low, high = find_level(l, h)
    tmp = []
    with open("./data/level_%02d.csv" % level, 'r') as r:
        reader = csv.reader(r, delimiter=',')
        for i, line in enumerate(reader):
            if i < low:
                continue
            elif i > high:
                break
            else:
                tmp.append(int(line[0]))
        return tmp, level

def get_no_compress_idx(a, value, center_orig):
    pos = [i for i, val in enumerate(a[0]) if val == value].index(center_orig) + 1
    with open("./data/level_00.csv", 'r') as r:
        reader = csv.reader(r, delimiter=',')
        count = 0
        center = 0
        for i,j in enumerate(reader):
            if count == pos:
                return center
            if int(j[0]) == value:
                center = i
                count+=1
        return -1
# TODO: Make this algorithm more efficient
def center_radius(l):

    a = query_range(0, l)
    center_orig = int(st.slider("Center", 0, len(a[0]), 0))
    radius_orig = int(st.slider("Radius", 0, center_orig + 1, 0))
    if (radius_orig == 0):
        df = pd.DataFrame({"data": a[0]})
        st.line_chart(df)
    else:
        value = int(a[0][center_orig])
        print(value)
        idx = get_no_compress_idx(a, value, center_orig)
        low = idx - radius_orig
        high = idx + radius_orig
        b = (query_range(low, high))
        df = pd.DataFrame({"data": b[0]})
        st.line_chart(df)


def main():
    l = 21339392
    center_rad = st.checkbox("Display Center/Radius")
    if center_rad:
        center_radius(l)
    else:
        minv = int(st.slider("Minimum Value for Zoom", 0,l,0))
        maxv = int(st.slider("Maximum Value for Zoom", g_max_value, l, l))
        a = query_range(minv, maxv)
        st.subheader(("Current compression level: %d" % a[1]))
        df = pd.DataFrame({"data": a[0]})
        st.line_chart(df)


if __name__ == "__main__":
    main()

# 252 - 366
