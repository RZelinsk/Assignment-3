# This is Problem 8

#import Counter
import re
import collections

#c = Counter()
def process_file(filename):
    #Open the file
    with open(filename) as f:
        lines = f.readlines()
        # Read each individual line using '\n'
        # Can also do rstrip because whitetext is behind text
        lines = [line.strip('\n') for line in open(filename)]
        print (lines)
    # ['I have a dream', 'chloe is the best', 'macs rule']
    # define an array here
    # for line in lines:
        # do things to each lines
        # split
        # make everything uppercase or lowercase
        # remove punctuation
process_file('speech.txt')
