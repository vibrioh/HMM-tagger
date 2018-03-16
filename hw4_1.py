#! /usr/bin/python

__author__ = "Jun Hu <jh3846@columbia.edu>"
__data__ = "$Oct 2, 2017"

import sys
from collections import defaultdict

'''
replace_rare is used to replace the words in train files such as 'ner_train.dat' which occur less than 5 times in the \
count files such as 'ner.counts', and output processed train data such as 'ner_train.dat.rare_processed'

1. prerequisite file:
python count_freqs.py ner_train.dat > ner.counts

2. typical usage:
python hw4_1.py ner.counts ner_train.dat > ner_train.dat.rare_processed

'''
def replace_rare(counts, train, output):
    # dict to store all words counts
    cnt_dict = defaultdict(int)

    # count all words and store results
    for l in counts.read().splitlines():
        line = l.strip().split(' ')
        if line[1] == 'WORDTAG':
            cnt_dict[line[3]] += int(line[0])

    # replace words in train files with '_RARE_'
    for l in train.read().splitlines():
        line = l.strip().split(' ')
        if line[0] == '':
            output.write('\n')
        elif cnt_dict[line[0]] < 5:
            output.write('_RARE_ ' + line[1] + '\n')
        else:
            output.write(l + '\n')

if __name__ == "__main__":
    with open(sys.argv[1], "r") as counts:
        with open (sys.argv[2], "r") as train:
            replace_rare(counts, train, sys.stdout)