import random
from enum import Enum
import math
NUM_VALS = 300

class Node:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    @staticmethod
    def init_node_array(data):
        ret = []
        for i in range(0, len(data)-1, 2):
            if (data[i] < data[i+1]):
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
    @staticmethod
    def decompress_node_array(data):
        ret = []
        for i in data:
            ret.append(i.low)
            ret.append(i.high)
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


def bar(root, barNumber):
    try:
        tmp = root
        for i in range(barNumber):
            tmp = tmp.next
        return tmp.layer
    except Exception as e:
        import sys
        print("ERROR: Quieried bar `%d` was too large for selected data. Please limit queries to the number of bars for the hierarchy" % barNumber)
        sys.exit(1)
class Box_Type(Enum):
    LEFT=1
    RIGHT=2
    CENTER=3

def box(vals, box_size, box_type):
    if box_type==Box_Type.LEFT:
        return vals[0:box_size]
    elif box_type==Box_Type.RIGHT:
        return vals[-box_size:]
    elif box_type==Box_Type.CENTER:
        size = len(vals)
        disp = box_size//2
        return vals[size-disp-2:size+disp+2]
def main():
   data = list(range(NUM_VALS))
   # for i in range(NUM_VALS):
       # data.append((random.random() * NUM_VALS - 1) + 1)

   data = (Node.init_node_array(data))
   root = Hierarchy.build_hierarchy(data)
   # Hierarchy.print_h(root)
   print("There are " + str(int(math.log(len(data), 2))) + " bars to choose from")
   dat = (bar(root, int(input("The larger the bar is, the finer the resulting data is. For example, in a scenario where there are 5 bars, bar 5 would contain the most amount of data, and bar 0 would contain the least amount of data: "))))
   print(Node.decompress_node_array(dat))
   
if __name__ == '__main__':
    main()
