import csv
import math
import pandas as pd
import os
import streamlit as st
import sys
from confparser import parse
g_max_value = int(parse('GRAPH_MAX_VALUE'))

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
    with open("../data/level_%02d.csv" % level, 'r') as r:
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
    with open("../data/level_00.csv", 'r') as r:
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
def center_radius(l, center_param=None, rad_param=None, idx=None):
    a = query_range(0, l)
    if(rad_param == 0):
        df = pd.DataFrame({"data": a[0]})
        st.line_chart(df)
    elif(not rad_param and not center_param):
        center_orig = int(st.slider("Center", 0, len(a[0]), 0))
        radius_orig = int(st.slider("Radius", 0, center_orig + 1, 0))
        if(radius_orig == 0):
            df = pd.DataFrame({"data": a[0]})
            st.line_chart(df)
        else:
# Center radius mode
            value = int(a[0][center_orig])
            idx = get_no_compress_idx(a, value, center_orig)
            low = idx - radius_orig
            high = idx + radius_orig
            b = (query_range(low, high))
            st.subheader(("Current compression level: %d" % b[1]))
            timeticks = range(center_orig - radius_orig, center_orig + radius_orig + 1)
            print(len(timeticks), len(b[0]))
            df = pd.DataFrame({"x": timeticks, "y": b[0]}, columns = ['x', 'y']).set_index('x')
            st.line_chart(df)
    else:
        if idx:
# Anomalous points mode
            radius_orig = rad_param
            low = idx - radius_orig
            high = idx + radius_orig
            # g_max_value = 5000
            # 5000 -> low - high -> 2
            # val <= 2499
            b = (query_range(low, high))
            timeticks = range(idx - radius_orig, idx + radius_orig + 1)
            print(len(timeticks), len(b[0]), len(b[0]))
            df = pd.DataFrame({"x": timeticks, "y": b[0]}, columns = ['x', 'y']).set_index('x')
            st.line_chart(df)
        else:
            center_orig = center_param
            radius_orig = rad_param
            value = int(a[0][center_orig])
            idx = get_no_compress_idx(a, value, center_orig)
            low = idx - radius_orig
            high = idx + radius_orig
            b = (query_range(low, high))
            st.subheader(("Current compression level: %d" % b[1]))
            df = pd.DataFrame({"data": b[0]})
            st.line_chart(df)

def read_anomalous_points(filepath):
    with open(filepath, "r") as f:
        reader = csv.reader(f, delimiter="\n")
        vals = []
        for i in reader:
            vals.append((list(map(int, i[0].split(',')))))
        return vals

def main():
    l = int(sys.argv[1]);
    options = ["Display Range", "Display Center/Radius", "Display Anomalous Points"]
    radio_group = st.radio("Graph Modes", options);
    current_option = options.index(radio_group)
    if current_option == 0:
        minv = int(st.slider("Minimum Value for Zoom", 0,l,0))
        maxv = int(st.slider("Maximum Value for Zoom", g_max_value, l, l))
        a = query_range(minv, maxv)
        st.subheader(("Current compression level: %d" % a[1]))
        df = pd.DataFrame({"data": a[0]})
        st.line_chart(df)
    elif current_option == 1:
        center_radius(l)
    else:
        points = read_anomalous_points("../" + parse("SOURCE_DIR") + "/anomalous_points.csv")
        tmp = ["y = " + str(i[0]) for i in points]
        tmp.append("Reset")
        sub_radio_group = st.radio("Anomalous Points", tmp)
        if sub_radio_group == "Reset":
            center_radius(l, rad_param=0)
        else:
            val = (tmp.index(sub_radio_group))
            conf_rad_param = int(parse("DEFAULT_RADIUS"))
            if conf_rad_param >= (g_max_value // 2):
                raise ValueError("DEFAULT_RADIUS is greater than GRAPH_MAX_VALUE. Please change vars.conf accordingly")
            center_radius(l, center_param=1, rad_param=, idx=points[val][1])
        


if __name__ == "__main__":
    main()

