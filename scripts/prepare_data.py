#!/usr/bin/python3
import json
import os
with open('../config/INFO.json') as f:
    data = json.load(f)

source = data['source']


os.system('curl %s -o out.csv' % source)
