#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

# create bar graph
graphItems = sorted(sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)[:10], key=lambda x: x[1])
        #[:10] returns first ten items

graph_x, graph_y = [*zip(*graphItems)]
plt.bar(graph_x, graph_y)
plt.xticks(range(len(graph_x)), graph_x)

x_label = "Language" if args.input_path == "reduced.lang" else  "Country" if args.input_path == "reduced.country" else ""
key = args.key
title = 'Number of times "' +key+'" was used in each '+x_label
plt.xlabel(x_label)
plt.ylabel("Count")
plt.title(title)
plt.savefig(x_label+"."+key+'.graph.png')
