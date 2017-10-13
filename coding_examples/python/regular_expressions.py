"""
These are some common examples for regular expressions in python
"""

import re

# starts with a lowercase or uppercase letter
letters = re.compile("(^[a-zA-Z])")

# is a number, including scientific notation
numbers = re.compile("(^(?:[+\-])?(?:\d*)(?:\.)?(?:\d*)?(?:[eE][+\-]?\d*$)?)")

# is a blank line
empty = re.compile("(^\s*$)")

# token for splitting lines
token = '\s+|(?<!\d)[,](?!\d)'



# if you just call this file, examples are returned
if __name__ == "__main__":

    numberline = "DISPX_C_0 -9.096348e+01 -2.222837e-06 1.884807e-07 1.837376e-09 -4.447534e-10 5.265927e-12"
    print("Example of detecting numbers in a line:\n{}\n".format(numberline))
    line = re.split(token, numberline.strip())
    print("Line was split into: \n{}".format(line))
    numlist=[]
    for item in line:
        if numbers.fullmatch(item):
            numlist.append(eval(item))
    print("Numlist created: {}".format(numlist))

