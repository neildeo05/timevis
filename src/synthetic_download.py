import csv
import random
import confparser
def main():
    num_timeticks = 21339392
    with open('../' + parse('SOURCE_DIR') + "/" + parse("SOURCE_FILE"), 'w') as f:
        t = csv.writer(f, delimiter=',')
        for i in range(num_timeticks):
              t.writerow([random.randint(0, 5000)])
    
if __name__ == "__main__":
    main()
