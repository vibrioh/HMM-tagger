#! /usr/bin/python

__author__ = "Jun Hu <jh3846@columbia.edu>"
__data__ = "$Oct 2, 2017"

import sys
from collections import defaultdict
import math

'''
given any trigrams, such as 'trigrams.txt', generate probabilities for each trigrams.

1. prerequisite file:
4_1.txt trigrams.txt 

2. typical usage:
python hw5_1.py 4_1.txt trigrams.txt > 5_1.txt
'''
def calc_tri_p(counts, trigrams, output):
    # dict of n-grams counts
    cnt_dict = defaultdict(int)
    # dict of trigrams probabilities
    tri_p_dict = defaultdict(float)

    # count the n-grams
    for l in counts.read().splitlines():
        line = l.strip().split(' ')
        if line[1] in {'2-GRAM', '3-GRAM'}:
            cnt_dict[tuple(line[2:])] = int(line[0])

    # calculate trigrams probabilities
    for k, v in cnt_dict.items():
        if len(k) == 3:
            tri_p_dict[k] = math.log(float(v) / float(cnt_dict[k[:-1]]), 2)

    # output results
    for l in trigrams.read().splitlines():
        line = tuple(l.strip().split(' '))
        if line in tri_p_dict.keys() and tri_p_dict[line] != 0:
            output.write(l + ' ' + str(tri_p_dict[line]) + '\n')
        else:
            output.write(l + ' -inf' + '\n')

if __name__ == "__main__":
    with open(sys.argv[1], "r") as counts:
        with open (sys.argv[2], "r") as trigrams:
            calc_tri_p(counts, trigrams, sys.stdout)
