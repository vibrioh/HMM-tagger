#! /usr/bin/python

__author__ = "Jun Hu <jh3846@columbia.edu>"
__data__ = "$Oct 2, 2017"

import sys
from collections import defaultdict
import math

'''
viterbi tagger, read count files such as '4_1.txt', and test data such as 'ner_dev.dat', and return the tags.

1. prerequisite:
4_1.txt 

2. typical usage:
python hw5_2.py 4_1.txt ner_dev.dat > 5_2.txt
'''

def viterbi_tagger(counts, ner_dev, output):

    # word counts
    cnt_xy = defaultdict(dict)
    # grams counts
    cnt_grams = defaultdict(int)
    # e(x|y)
    e = defaultdict(float)
    # q(u, v, w)
    q = defaultdict(float)
    # possible tags
    K = set()

    # read count file and count words and n-grams
    for l in counts.read().splitlines():
        line = l.strip().split(' ')
        if line[1] == 'WORDTAG':
            cnt_xy[line[2]][line[3]] = int(line[0])
            cnt_grams[line[3]] += int(line[0])
            K.add(line[2])
        if line[1] in {'1-GRAM', '2-GRAM', '3-GRAM'}:
            cnt_grams[tuple(line[2:])] = int(line[0])

    # calculate e(x|y)
    for y in cnt_xy.keys():
        cnt_y = sum(cnt_xy[y].values())
        for x in cnt_xy[y].keys():
            e[(x, y)] = float(cnt_xy[y][x]) / float(cnt_y)

    # calculate q(u, v, w)
    for k, v in cnt_grams.items():
        if type(k) == tuple and len(k) == 3:
            q[k] = float(v) / float(cnt_grams[k[:-1]])

    # get the list of all sentences, and the list of words in a sentence.
    sentence = []
    SS = []
    for l in ner_dev.read().splitlines():
        line = l.strip().split(' ')
        if line[0] =='':
            SS.append(sentence)
            sentence = []
        else:
            sentence.append(line[0])

    # for each sentence
    for s in SS:
        s_org = s
        s = []
        # unseen replace with '_RARE_'
        for word in s_org:
            if cnt_grams[word] == 0:
                s.append("_RARE_")
            else:
                s.append(word)
        # pi(k, u, v)
        pi = defaultdict(int)
        # backpointers
        bp = defaultdict(str)
        pi[(0, "*", "*")] = 1
        n = len(s)

        # dynamically get max pi and keep backpointers
        for k in range(1, n + 1):
            for v in K:
                for u in K if k > 1 else {'*'}:
                    for w in K if k > 2 else {'*'}:
                        k_prob = pi[(k - 1, w, u)] * q[(w, u, v)] * e[(s[k - 1]), v]
                        if k_prob > pi[(k, u, v)]:
                            pi[(k, u, v)] = k_prob
                            bp[(k, u, v)] = w
        # return list of tags Y
        Y = []
        # return list of log probabilities
        P_log = []

        n_prob = 0
        y_n = ''
        y_n_1 = ''

        # get yn y(n-1)
        for u in K if n > 1 else {'*'}:
            for v in K:
                if pi[(n, u, v)] * q[(u, v, "STOP")] > n_prob:
                    n_prob = pi[(n, u, v)] * q[(u, v, "STOP")]
                    y_n = u
                    y_n_1 = v
        v = y_n_1
        u = y_n
        p_n_1 = math.log(n_prob, 2)
        p_n = math.log(pi[(n, u, v)], 2)
        Y.append(v)
        Y.append(u)
        P_log.append(p_n_1)
        P_log.append(p_n)

        # get all ys in Y through the backpointer
        for k in range(n, 1, -1):
            w = bp[(k, u, v)]
            Y.append(w)
            log_p = math.log(pi[(k - 1, w, u)], 2)
            P_log.append(log_p)
            v = u
            u = w

        Y.reverse()
        P_log.reverse()

        # output the tags for the sentence
        for count, word in enumerate(s_org):
            output.write(str(word) + ' ' + str(Y[count + 1]) + ' ' + str(P_log[count]) + '\n')
        output.write('\n')

if __name__ == "__main__":
    with open(sys.argv[1], "r") as counts:
        with open (sys.argv[2], "r") as ner_dev:
            viterbi_tagger(counts, ner_dev, sys.stdout)