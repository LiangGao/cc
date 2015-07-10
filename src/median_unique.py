# word count project part 2
#
# Liang Gao
#
# Calculate the median number of unique words per tweet, and update this median as tweets come in. The
# program also returns the total run time.
#
# usage: ./median_unique.py inputfile outputfile
# example: ./median_unique.py in.txt out.txt
#
# The function 'print_median_unique' loads a text file, counts the unique words, calculates the median
# value of unique words per line, and updates this median as lines (tweets) come in.

import heapq
import time
import sys

def print_median_unique(inputfile, outputfile):
    # num_unique = [] # list for number of unique words for each line
    m = []             # for storing the median values
    hmax = []          # max heap, the left branch
    hmin = []          # min help, the right branch
    n = 1;
    f_in = open(inputfile,'rU')    # read the data
    f_out = open(outputfile,'wt')  # make the txt file for unique words

    for line in f_in:
        words = line.split()   # split the line into list of words by whitespace
        uni_words = []         # list of the unique words for current line
        uni_count = 0          # number of the unique words for current line
        for word in words:
            # word = word.lower()     # change all the words to lower case
            if not word in uni_words: # count unique word for current line
                uni_count = uni_count + 1
                uni_words.append(word)
        if uni_count != 0:     # situation when current line is empty
            # using heap data structrue to find the median value
            
            # push new value into either branch
            value = uni_count
            if n == 1:          # the first value
                heapq.heappush(hmin,value)
            elif n == 2:        # the second value 
                if value <= hmin[0]:
                    heapq.heappush(hmax, -value)   # negative sign is added so that heap returns max
                else:
                    heapq.heappush(hmax, -hmin[0]) # negative sign added for max heap
                    heapq.heappushpop(hmin, value)
            else:               # for the rest values
                if value >= hmin[0]:
                    heapq.heappush(hmin, value)
                else:
                    heapq.heappush(hmax, -value)   # negative sign added for max heap
            n = n + 1;

            # balance the whole heap so that it's centered
            while len(hmin) - len(hmax) > 1:
                heapq.heappush(hmax, -heapq.heappop(hmin))
            while len(hmax) - len(hmin) > 1:
                heapq.heappush(hmin, -heapq.heappop(hmax))

            # calculate median
            if len(hmin) == len(hmax):  # total number of lines is even
                m.append((- hmax[0] + hmin[0])/2.0)
            elif len(hmin) - len(hmax) == 1:
                m.append(hmin[0])           # return the root of the longer branch
            elif len(hmin) - len(hmax) == -1:
                m.append(-hmax[0])          # return the root of the longer branch

            f_out.write('%.2f \n' %(m[n-2]))
    f_out.close()
    f_in.close()
    return
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'usage: median_unique.py inputfile outputfile'
        sys.exit(1)

    start_time = time.time()
    input_name = sys.argv[1]
    output_name = sys.argv[2]
    print_median_unique(input_name, output_name)
    print("total run time for median unique:  %.4f seconds " % (time.time() - start_time))