#!/usr/local/bin/python

# Workflow in programming

"""
Specifically, we will be using these examples to understand basic
programming workflow in Python, though this can (mostly) be also applied
to R and other programming languages as well
"""

# if else statements
"""
if else statements in R used parens and brackets to clearly represent blocks of code:

if (a == 1) {
  print('bananas!')
} else if (a == 2) {
  print('oranges!')
} else {
  print('no bananas or oranges!')
}

Python uses less writing but is bound to spacing and return carriages
"""

# Multiple object assignment
x, y = False, False
# Python uses no parens or brackets, and the if-else ends at an empty line
if x:
  print 'apple'
elif y:
  print 'banana'
else:
  print 'sandwich'


# while loops
"""
while loops excute blocks of code while some condition is true.
in R:
N <- 20
i <- 1
while (i <= N) {
    y <- i*i
    i <- i + 1
}
"""
x = 0
while True:
  print 'Hello!'
  x += 1
  if x>= 3:
    break


# For loops are similar, and are predetermined loops
for k in range(4):
  print k**2


# try and except are very useful for handing errors
try:
  print undef
except:
  print 'nice try'


# Functions
"""
in R:
subtract.three <- function(x) {
  x - 3
}
"""
def x_minus_3(x):
  return x - 3

