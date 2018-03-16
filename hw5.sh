#!/usr/bin/env bash


# Question 5
echo ------------------------- Question 5 ----------------------------

echo ------------------------- generate  5_1.txt ----------------------------

python hw5_1.py 4_1.txt trigrams.txt > 5_1.txt

echo ------------------------- 5_1.txt is ready ----------------------------

echo ------------------------- generate  5_2.txt ----------------------------

python hw5_2.py 4_1.txt ner_dev.dat > 5_2.txt

echo ------------------------- 5_1.txt is ready ----------------------------

echo ------------------------- evaluate 5_2.txt ----------------------------

python eval_ne_tagger.py ner_dev.key 5_2.txt

echo ------------------------- q5_done ----------------------------