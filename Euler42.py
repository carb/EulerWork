#!/usr/bin/python
#problem 42
from Euler42words import getwords
import time
#from problem 22 [Euler22.py]
def string_score(string):
  strsum = 0
  for letter in string:
    strsum += ord(letter)-64
  return strsum

def listTriNumbers(number):
  nums = []
  for num in range(1,number+1):
    nums.append(int(.5*(num*(num+1))))
  return nums
tStart = time.time()
trianglenumbers = listTriNumbers(300)
words = getwords()
total = 0
for word in words:
  score = string_score(word)
  if score in trianglenumbers:
    total+=1
print "Run Time = " + str(time.time() - tStart)
print total


