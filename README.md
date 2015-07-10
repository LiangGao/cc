Coding Challenge
===========================================================

For this coding challenge, a few functions were developed to help analyze the community of Twitter users.  For simplicity, the features are primitive. The functions here should also work with ordinary text file.

## Challenge Summary
This challenge is to implement two following features:

1. Calculate the total number of times each word has been tweeted.
2. Calculate the median number of *unique* words per tweet, and update this median as tweets come in.

The description repo for this Coding Challenge is [here](https://github.com/InsightDataScience/cc-example).

## Details of Implementation

There are two .py file in the `src` directory, `words_tweeted.py` and `median_unique.py`, for each feature mentioned above. The `run.sh` loads the `tweets_test_data.txt` from `tweet_input`, feeds the data to both programs in `src` directory, and writes the result into `ft1.txt` (feature 1) and `ft2.txt` (feature 2) in the `tweet_output` directory.

The program is written in Python, with `time`, `sys`, and `heapq` module imported. The `time` module is used only to estimate the run time of each program, and `heapq` module is used to calculate median for the second feature.

The program has been tested with data of different sizes to show that it scales for large amounts of data. The largest data set was 571MB, with approximately 5,150,000 tweets. The test was perform on a MacBook Air (i5 1.6G/4G/128G). The following figure shows the run time for the two functions. (No, it's not a 3D plot so no need for your 3D glass)

![Example Repo Structure](plots/cc_time.png)

The second feature is essentially a `running median` problem. One suitable approach is to use a `two-heap` based queue and return one root, or mean of the two roots, as the median, after balancing the queue. This method has time efficiency of O(n), as shown in the figure above.

## Some other Thoughts

The two-heap based method here is good for general purpose of calculating running median. However, for this specific problem, there is a possibly better approach.

Because the word-limit for each tweet is 140, the maximum number of unique words per tweet is 140. This means we just need to *locate* the median for a numerical list/array including only integers 1 to 140. It can be done using the `dictionary` in python, with keys equal to the possible numbers of unique words per tweet (1 - 140), and values equals to the appearances.

Another problem of the two-heap based method is that it may cause memory leak, especially when it's used for live web data analysis. One the other hand, the dictionary based method won't be the same efficient when handling situations with unlimited keys, such as float numbers.

L_20150710
