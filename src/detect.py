import csv
from isolation_forests import find_anomalies
from confparser import parse, parse_path
#TODO: Clean this up
def main():
    if parse_path("../vars.conf","DEFAULT",'COMPRESS_MODE') == 'all':
        # make parsing faster, because at least 5 anomalies will reside in level_05 that would be present in level_00 (min/max combo)
        filename = '../data/level_05.csv'
    else:
        filename = '../data/level_00.csv'
    anomalies = find_anomalies(filename, 5)
    with open("../" + parse("SOURCE_DIR") + "/" + "anomalous_points.csv", "w") as t:
        with open("../data/level_00.csv", 'r') as fg:
            reader = csv.reader(fg, delimiter=',')
            tg = [int(i[0]) for i in reader]
        w = csv.writer(t, delimiter=',')
        for i in anomalies:
            w.writerow([i, tg.index(i)])
    print("DONE WRITING TO FILE")
        



if __name__ == "__main__":
    main()
