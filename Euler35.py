#!/usr/bin/python
def rotatenum(number):
  newnum = str(number)
  templist = []
  for i in newnum:
    newnum = newnum[1:] + newnum[0]
    templist.append(int(newnum))
  return set(templist)

def era2(n):
  siv=range(n+1)
  siv[1]=0
  sqn = int(round(n**0.5))
  for i in range(2,sqn+1):
    siv[2*i:n+1:i]=[0]*(n/i-1)
  return filter(None,siv)

primes = era2(1000000)
primeset = set(primes)
primelist = []
import time
tstart = time.time()
for prime in primes:
  if rotatenum(prime) <= primeset:
    primelist.append(prime)
print len(primelist)
print "time =", time.time()-tstart


