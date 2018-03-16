#! /usr/bin/python

__author__ = "Jun Hu <jh3846@columbia.edu>"
__data__ = "$Oct 2, 2017"

import sys
from collections import defaultdict
import re

def replace_rare(counts, train, output):
    cnt_dict = defaultdict(int)

    for l in counts.read().splitlines():
        line = l.strip().split(' ')
        if line[1] == 'WORDTAG':
            cnt_dict[line[3]] += int(line[0])

    for l in train.read().splitlines():
        line = l.strip().split(' ')
        if line[0] == '':
            output.write('\n')
        elif cnt_dict[line[0]] < 5:
            output.write(classify_rare(line[0]) + ' ' + line[1] + '\n')
        else:
            output.write(l + '\n')
'''
classify_rare is added to the original replace_rare, and added 12 more tags according to their pattern.

1. prerequisite file:
python count_freqs.py ner_train.dat > ner.counts

2. typical usage:
python hw6_classifier.py ner.counts ner_train.dat > ner_train.dat.classifier_processed
python count_freqs.py ner_train.dat.classifier_processed > 6_classifier_processed.txt
'''
def classify_rare(word):
    p1 = re.compile('^[0-9]+$')
    p2 = re.compile('^[-+]?[0-9]+$')
    p3 = re.compile('^[a-z]+$')
    p4 = re.compile('^[A-Z]+$')
    p5 = re.compile('^[A-Z][a-z]+$')
    p6 = re.compile('([A-Z]\.)+ ')
    p7 = re.compile('\w+(-\w+)* ')
    p8 = re.compile(' \$?\d+(\.\d+)?%? ')
    p9 = re.compile(' \.\.\. ')
    if p1.match(word):
        if len(word) == 2:
            return '_NUM_2_'
        elif len(word) == 4:
            return '_NUM_4_'
        else:
            return '_NUM_'
    elif p2.match(word):
        return '_NUM_sci_'
    elif p3.match(word):
        if len(word) == 1:
            return '_CHAR_'
        else:
            return '_VOCA_'
    elif p4.match(word):
        return '_allCAPs_'
    elif p5.match(word):
        return '_allCAPs_'
    elif p6.match(word):
        return '_ABBR_'
    elif p7.match(word):
        return '_HYP_'
    elif p8.match(word):
        return '_CURR_'
    elif p9.match(word):
        return '_ELLI'
    else:
        return '_RARE_'

if __name__ == "__main__":
    with open(sys.argv[1], "r") as counts:
        with open (sys.argv[2], "r") as train:
            replace_rare(counts, train, sys.stdout)