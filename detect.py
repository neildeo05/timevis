import csv
import heapq 
def main():
    filename = './data/level_00.csv'
    with open(filename, "r") as f:
        r = csv.reader(f, delimiter=',')
        t = [int(i[0]) for i in r]
        with open("./data/level_14.csv", 'r') as fg:
            rg = csv.reader(fg, delimiter=',')
            tg = [int(i[0]) for i in rg]
            large = [[tg.index(i), t.index(i)] for i in heapq.nlargest(5, tg)]
            small = [[tg.index(i), t.index(i)] for i in heapq.nsmallest(5, tg)]
    with open("anomalous_points.csv", 'w') as t:
        w = csv.writer(t, delimiter=',')
        w.writerows(small)
        w.writerows(large)

if __name__ == "__main__":
    main()
