import csv
import backend
import os

def read_csv(filename):
    # Open file as IO object
    with open(filename, 'r') as csv_file:
        # Initialize csv_reader with the IO object of the file passed in as a parameter
        csv_reader = csv.reader(csv_file, delimiter = '\n')
        # The csv_reader is iterable, so list(csv_reader) turns the data of the file into a list and returns it.
        # In order to return a list of ints, the items in the list have to be converted to ints, so map(int, list) does that
        # return list(map(int, list(csv_reader)))
        return list(csv_reader)

def build_tree(data):
    # This function converts the raw_data (of type list) into a hierarchy (tree/graph)
    return backend.query_select_data(data)

def write(root, levels):
    os.chdir("data")
    tmp = root
    basename = "level_%02d.csv"
    for i in range(levels+2):
        with open(basename % i, 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter = ',')
            csv_writer.writerow(backend.convert_node_array_to_list(tmp.layer,backend.Decompress_Arg.ALL))
        tmp = tmp.next


if __name__ == "__main__":
    raw_data = read_csv("top100k.csv")
    print(len(raw_data))
    root = build_tree(raw_data)
    write(*root)
    # backend.Hierarchy.print_h(root[0])

    # write()
