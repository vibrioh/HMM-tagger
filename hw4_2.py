#! /usr/bin/python

__author__ = "Jun Hu <jh3846@columbia.edu>"
__data__ = "$Oct 2, 2017"

import math
import sys

'''
the tagger uses only e(x|y)

1. prerequisite file:
python count_freqs.py ner_train.dat.rare_processed > 4_1.txt

2. typical usage:
python hw4_2.py 4_1.txt ner_dev.dat > 4_2.txt
'''

def baseline_tagger(f_counts, ner_dev, prediction):

    # read files
    counts = f_counts.read().splitlines()
    dev = ner_dev.read().splitlines()

    # set of all words have seen
    Words = set()
    # tags and their counts
    Count_tags = {}
    # emissions of possible
    Count_emss = {}

    # count tags in count file
    for str_counts in counts:
        ls_counts = str_counts.strip().split()
        if ls_counts[1] == 'WORDTAG':
            Words.add(ls_counts[3])
            if ls_counts[2] in Count_tags:
                Count_tags[ls_counts[2]] += int(ls_counts[0])
            else:
                Count_tags[ls_counts[2]] = int(ls_counts[0])

    # calculate emission for each possible e(x|y)
    for str_counts in counts:
        ls_counts = str_counts.strip().split()
        if ls_counts[1] == 'WORDTAG':
            Count_emss[ls_counts[3] + ' ' + ls_counts[2]] = math.log(float(ls_counts[0])/float(Count_tags[ls_counts[2]]), 2)

    # calculate the max e(x|y) for '_RARE_'
    _RARE_pre = float('-inf')
    _tag = 'unassigned'
    for tag in Count_tags:
        word_tag_tmp = '_RARE_' + ' ' + tag
        if (word_tag_tmp in Count_emss) and Count_emss[word_tag_tmp] > _RARE_pre:
            _tag = tag
            _RARE_pre = Count_emss[word_tag_tmp]
    _RARE_emss = ' ' + _tag + ' ' + str(_RARE_pre) + '\n'

    # predict tag with only e(x|y)
    for word in dev:
        if word in Words:
            word_tag = word + ' ' + 'tag_unassigned'
            pre = float('-inf')
            for tag in Count_tags:
                word_tag_tmp = word + ' ' + tag
                if (word_tag_tmp in Count_emss) and Count_emss[word_tag_tmp] > pre:
                    word_tag = word_tag_tmp
                    pre = Count_emss[word_tag_tmp]
            prediction.write(word_tag + ' ' + str(pre) + '\n')
        elif word == '':
            prediction.write('\n')
        else:
            prediction.write(word + _RARE_emss)

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f_counts:
        with open (sys.argv[2], "r") as ner_dev:
            baseline_tagger(f_counts, ner_dev, sys.stdout)
