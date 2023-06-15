#!/usr/bin/env python

import string
import os

directory = "result/solve-loop/"
path_names = [x[0] for x in os.walk(directory)]

result = {}
for p in path_names:
    if p == directory:
        continue
    try:
        with open(p+"/result.txt") as f:
            lines = f.readlines()
            t = lines[-1].strip().split(" ")[-1]

            if t != "failed" and t == "normally.":
                unsolved_pairs = lines[-2].strip()

                pairs = []
                i = 0
                print(unsolved_pairs)
                while i < len(unsolved_pairs):
                    print("right now at {} which is {}".format(i, unsolved_pairs[i]))
                    if unsolved_pairs[i] in [',','[', ' ', '"']:
                        i += 1
                        continue
                    if unsolved_pairs[i] == ']':
                        break

                    start = i
                    while (unsolved_pairs[i]!=','):
                        i+=1
                    t1= unsolved_pairs[start:i]
                    i+=1
                    start = i
                    while (unsolved_pairs[i]!='"'):
                        i+=1
                    t2= unsolved_pairs[start:i]
                    print("====", t1,t2)

                    pairs.append((t1,t2))
                    i+=3

                result[p] = { "result" : "okay",
                             "unsolved number": lines[-4].strip().split()[-1],
                             "unsolved pairs":  pairs
                             }
    except:
        continue

from pprint import pprint as pr
pr(result)


print("total numbers of fonts", len(result))
average_number = sum([ float(result[r]["unsolved number"]) for r in result]) / len(result)
print("average", average_number)

import pandas as pd
import matplotlib.pyplot as plt

# test dataframe
df = pd.DataFrame({
    'pairs': [ 
        ["{}{}".format(p[0], p[1]) for p in result[r]["unsolved pairs"] ]
        for r in result ],
    'numbers': [ 
        result[r]["unsolved number"]
        for r in result ],
                   
               })

# use explode to expand the lists into separate rows
dfe = df.numbers.explode().to_frame().reset_index(drop=True)

# groupby the values in the column, get the count and sort
dfg = dfe.groupby('numbers').numbers.count() \
                               .reset_index(name='count') \
                               .sort_values(['count'], ascending=False) \
                               .head(10).reset_index(drop=True)

# plot the dataframe
dfg.plot.bar(x='numbers').get_figure().savefig('number.png')

# use explode to expand the lists into separate rows
dfe = df.pairs.explode().to_frame().reset_index(drop=True)

# groupby the values in the column, get the count and sort
dfg = dfe.groupby('pairs').pairs.count() \
                               .reset_index(name='count') \
                               .sort_values(['count'], ascending=False) \
                               .head(10).reset_index(drop=True)

# plot the dataframe
dfg.plot.bar(x='pairs').get_figure().savefig('count.png')

import seaborn as sns

# plot dfe
sns.countplot(x='pairs', data=dfe, order=dfe.pairs.value_counts().iloc[:20].index)
plt.xticks(rotation=90)
plt.savefig('count_result.png')
