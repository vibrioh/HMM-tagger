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

echo

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

echo

# Question 6
echo ------------------------- Question 6 ----------------------------

echo ------------------------- generate  ner_train.dat.classifier_processed ----------------------------

python hw6_classifier.py ner.counts ner_train.dat > ner_train.dat.classifier_processed

echo ------------------------- ner_train.dat.classifier_processed is ready ----------------------------

echo ------------------------- generate  6_classifier_processed.txt ----------------------------

python count_freqs.py ner_train.dat.classifier_processed > 6_classifier_processed.txt

echo ------------------------- 6_classifier_processed.txt is ready ----------------------------


echo ------------------------- generate  6.txt ----------------------------

python hw6.py 6_classifier_processed.txt ner_dev.dat > 6.txt

echo ------------------------- 6.txt is ready ----------------------------


echo ------------------------- evaluate 6.txt ----------------------------

python eval_ne_tagger.py ner_dev.key 6.txt

echo ------------------------- q6_done ----------------------------


