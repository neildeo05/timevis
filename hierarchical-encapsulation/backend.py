import random
from enum import Enum
import math
import numpy as np
class Box_Type(Enum):
    LEFT=1
    RIGHT=2
    CENTER=3
class Decompress_Arg(Enum):
    MIN=1
    MAX=2
    ALL=3

class Node:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    @staticmethod
    def init_node_array(data):
        ret = []
        for i in range(0, len(data)-1, 2):
            if data[i] < data[i+1]:
                ret.append(Node(data[i], data[i+1]))
            else:
                ret.append(Node(data[i+1], data[i]))
        return ret
    @staticmethod
    def node_array(data):
        ret = []
        for i in range(0, len(data) - 1, 2):
            tmp = [data[i].low, data[i].high, data[i+1].low, data[i+1].high]
            ret.append(Node(min(tmp), max(tmp)))
        return ret

        
    def __repr__(self):
        return "Node(" + str(self.low) + " " + str(self.high) + ")"
class Hierarchy:
    def __init__(self, layer, next):
        self.next = next
        self.layer = layer

    @staticmethod
    def build_hierarchy(data):
        combos = int(math.log(len(data), 2))
        root = Hierarchy(data, None)
        tmp = root
        for i in range(combos):
            tmp.next = Hierarchy(Node.node_array(tmp.layer), None)
            tmp = tmp.next
        return root 
    def __repr__(self):
        for i in self.layer:
            print(i)
        return "" + str(len(self.layer))
    @staticmethod
    def print_h(root):
        tmp = root
        while(tmp):
            print(tmp);
            print()
            tmp = tmp.next
def num_bars(length):
    return int(math.log(length, 2)) - 1

def bar(root, barNumber):
    try:
        tmp = root
        for i in range(barNumber):
            tmp = tmp.next
        return tmp.layer
    except Exception as e:
        print("Bar number too high")
        quit()
        
def box(vals, box_size, box_type):
    if box_type==Box_Type.LEFT:
        return vals[0:box_size]
    elif box_type==Box_Type.RIGHT:
        return vals[-box_size:]
    elif box_type==Box_Type.CENTER:
        size = len(vals)
        disp = box_size//2
        return vals[size-disp-2:size+disp+2]

def decompress_node_array(data, Decomp_Arg):
    vals = []
    if Decomp_Arg == Decompress_Arg.ALL:
        for c,i in enumerate(data):
            vals.append([c+1, i.low])
            vals.append([c+1, i.high])
        return (vals)
    elif Decomp_Arg == Decompress_Arg.MIN:
        for c,i in enumerate(data):
            vals.append([c+1, i.low])
        return (vals)
    elif Decomp_Arg == Decompress_Arg.MAX:
        for c,i in enumerate(data):
            vals.append([c+1, i.high])
        return (vals)

# TODO Query select data is very slow, most likely initting the node array and building the hierarrchy is very time consuming...
#      To fix -> optimize building hierarchy
def query_select_data(data, msg):
   data = Node.init_node_array(data)
   root = Hierarchy.build_hierarchy(data)
   dat = bar(root, int(msg))
   return dat


def filter_data(data, arg):
    return decompress_node_array(data, arg)

