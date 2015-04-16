#!/usr/local/bin/python

# Modules
"""
A file with Python code in it is referred to as a module. Modules can be turned into executable scripts in two steps:
1)  include the if __name__ == ‘__main__’ block
2)  specify the interpreter (typically using a Unix shebang) seem above
"""

from mrjob.job import mrjob

class MRHL(MRJob):

  def mapper(self, _, line):
    lat, lon, src, nuid = line.rstrip().split(',')
    if src == 'physical':
      yield nuid, (lon, lat)
    else:
      pass

  def reducer(self, nuid, lonlats):
    unique_lonlats = list(set([tuple(k) for k in lonlats]))
    yield nuid, len(unique_lonlats)

if __name__ == '__main__':
  MRHL.run()