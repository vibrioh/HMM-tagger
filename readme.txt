COMS W4705
Programming Homework 1

Jun Hu
jh3846

USAGES:
-------------------------------------------------
run_all.sh: -- for all submitted code testing
hw4.sh: -- test for question4
hw5.sh: -- test for question5
hw6.sh: -- test for question6
(input/output file names are used as instructed in piazza in all the shell script)


PERFORMANCE
--------------------------------------------------
__Q4__:

Found 14043 NEs. Expected 5931 NEs; Correct: 3117.

	 precision 	recall 		F1-Score
Total:	 0.221961	0.525544	0.312106
PER:	 0.435451	0.231230	0.302061
ORG:	 0.475936	0.399103	0.434146
LOC:	 0.147750	0.870229	0.252612
MISC:	 0.491689	0.610206	0.544574

Observations: Overall performance is very ugly. Because we only used e(x|y) to tag the test data. for any x, there can be only one maximum y to be tagged. No other information is involved. And lots of words are unseen in the train data, so they are replaced to '_RARE_' and been tagged to the same tagger. That can explain why the model is so poor, especially why there is so high NEs. However, interestingly, recall of 'LOC' is pretty high while its precision is very low, which may imply that 'LOC' is over-tagged to most of the words.

__Q5__:

Found 4704 NEs. Expected 5931 NEs; Correct: 3647.

	 precision 	recall 		F1-Score
Total:	 0.775298	0.614905	0.685849
PER:	 0.762535	0.595756	0.668907
ORG:	 0.611855	0.478326	0.536913
LOC:	 0.876458	0.696292	0.776056
MISC:	 0.830065	0.689468	0.753262

Observations: The performance is significantly improved by Viterbi. Now the NEs is lowed down. Although the correct is not improved much, the total NEs only found 4704, lesser than the expected. There is some space left for increasing NEs found, and overall performance can be improved more.

__Q6__:

Found 5799 NEs. Expected 5931 NEs; Correct: 4328.

	 precision 	recall 		F1-Score
Total:	 0.746336	0.729725	0.737937
PER:	 0.809524	0.776931	0.792893
ORG:	 0.543067	0.664425	0.597647
LOC:	 0.840438	0.752454	0.794016
MISC:	 0.834656	0.685125	0.752534

Observations: As mentioned before, based on Viterbi, classification of rare words significantly improved performance. We can find that the NEs are found 5799, very close to the 5931. And the correct NEs are 4328, overall F1-Score is 0.74, which means the classification is helpful. Especially, I used 12 different classes to cover the patterns like 'U.S.A', '1998', '98', 'one-third', 'CA$', '65%', 'abc', 'ABC', 'Abc', '...', '56789' and so on. I found capitalization tags like '_allCAPs_' and '_initCAPs_' are really functional well.