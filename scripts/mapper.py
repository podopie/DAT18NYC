# -*- coding: utf-8 -*-
import sys
import re

for line in sys.stdin:
    result = []
    # remove leading and trailing whitespace
    line = line.strip()
    # remove odd symbols from the text
    line = re.sub('[!"§$%&/()=?*#()\[\],.<>:;~_-]',"", line)
    # split the line into words
    words = line.split(" ")
    # insert the cleaned words into the results list
    for word in words:
        print word, 1
