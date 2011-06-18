#!/usr/bin/python
#this is just a straight brute force...
#thelist = [a**b for a in range(2,101) for b in range(2,101)]
#theset = set([a**b for a in range(2,101) for b in range(2,101)])
#theOneLine = ...
import time
tStart = time.time()
print len(set([a**b for a in range(2,101) for b in range(2,101)]))
print "Run Time = " + str(time.time() - tStart)
