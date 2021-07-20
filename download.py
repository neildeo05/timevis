import gdown
import sys

url = sys.argv[1]
output = 'data.csv'
gdown.download(url, output, quiet=False)
