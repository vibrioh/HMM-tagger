#!/usr/bin/env bash

echo ------------------------- generate ner.counts ----------------------------

python count_freqs.py ner_train.dat > ner.counts

echo ------------------------- ner.counts is ready ----------------------------

echo

# Question 4
echo ------------------------- Question 4 ----------------------------

echo ------------------------- generate  ner_train.dat.rare_processed ----------------------------

python hw4_1.py ner.counts ner_train.dat > ner_train.dat.rare_processed

echo ------------------------- ner_train.dat.rare_processed is ready ----------------------------


echo ------------------------- generate  4_1.txt ----------------------------

python count_freqs.py ner_train.dat.rare_processed > 4_1.txt

echo ------------------------- 4_1.txt is ready ----------------------------

echo ------------------------- generate  4_2.txt ----------------------------

python hw4_2.py 4_1.txt ner_dev.dat > 4_2.txt

echo ------------------------- 4_2.txt is ready ----------------------------

echo ------------------------- evaluate 4_2.txt ----------------------------

python eval_ne_tagger.py ner_dev.key 4_2.txt

echo ------------------------- q4_done ----------------------------




