# word count project part 1
#
# Liang Gao
#
# Calculate the total number of times each word has been tweeted. The program also returns
# the total run time.
#
# usage: ./words_tweeted.py inputfile outputfile
# example: ./words_tweeted.py in.txt out.txt
#
# The function 'word_count_dic' counts the total number of times each word appears in
# the input text file, and returns a dictionary of which the keys are the words and the
# values are the numbers of appearance for each key.
#
# The function 'cout_words' print out the result from word_count_dic to the output file.

import time
import sys

def word_count_dict(filename):
    word_count = {} # dictionary for counting words
    f_in = open(filename,'rU')          # read the data
    for line in f_in:
        words = line.split()   # split the line into list of words by whitespace
        for word in words:
            # word = word.lower()  # change all the words to lower case
            if word in word_count:  # count each word
                word_count[word] = word_count[word] + 1
            else:
                word_count[word] = 1
    f_in.close()
    return word_count
    
def count_words(inputfile, outputfile):
    word_count = word_count_dict(inputfile)
    words = sorted(word_count.keys())  # sort the words
    f_out = open(outputfile,'wt')
    for word in words:
        text = '{0:30} {1:5d}'.format(word, word_count[word])
        f_out.write(text+'\n')
    f_out.close()
    return
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'usage: ./words_tweeted.py inputfile outputfile'
        sys.exit(1)

    start_time = time.time()
    input_name = sys.argv[1]
    output_name = sys.argv[2]
    count_words(input_name, output_name)
    print("total run time for word count:  %.4f seconds " % (time.time() - start_time))
