#!/usr/bin/python
def decomp(number):
  temp = list(str(number))
  for n in range(len(temp)):
    temp[n] = int(temp[n])
  return temp

def sfn(num, separate): #Sum of Factorials of a Number
  sum1, o = 0, 0
  for n in separate:
    sum1 += factorials[n]
    if sum1 > num: #you went over...
      o = 1        #just quit now before you
      break        #make a fool of yourself
  return sum1 if o==0 else 0

factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]  
import time
tstart = time.time()
i = 2
while i<50000: #appropriate upper bound
  i += 1
  a = decomp(i)
  b = sfn(i,a)
  if b == i:
    print str(i)+":",b
print time.time()-tstart

#Time= 0.483063936234 seconds
#booyah
