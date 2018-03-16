#!/usr/bin/env bash


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

