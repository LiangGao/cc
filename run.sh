#!/bin/bash

# example of the run script for running the word count
# works only under Mac system, not for windows
# the first line calls words_tweeted.py, loads tweets.txt, and writes the output result in ft1.txt
# the first line calls median_unique.py, loads tweets.txt, and writes the output result in ft2.txt

python ./src/words_tweeted.py ./tweet_input/tweets_test_data.txt ./tweet_output/ft1.txt
python ./src/median_unique.py ./tweet_input/tweets_test_data.txt ./tweet_output/ft2.txt