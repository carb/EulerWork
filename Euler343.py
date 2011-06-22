#!/usr/bin/python
#just trying one of the newer ones out.
from fractions import Fraction,gcd

def f(k):
  tmpFrac = Fraction(1,k)
  while tmpFrac.denominator != 1:
    tmpFrac = Fraction(tmpFrac.numerator+1,tmpFrac.denominator-1)
  return tmpFrac.numerator

def era2(n):
  siv=range(n+1)
  siv[1]=0
  sqn = int(round(n**0.5))
  for i in range(2,sqn+1):
    siv[2*i:n+1:i]=[0]*(n/i-1)
  return filter(None,siv)

def red(n,d,gd):
  gd = gcd(n,d)
  if gd != 1:
    n /= gd
    d /= gd
  return n,d

def f2(k,dic):
  best, num, den, flist, fdict, bol = 0, 1, k, [], dic, True
  while den != 1:
    print num,den
    if num == 1:
      flist.append(den)
    if den&1==1:
      den = (den-1)>>1
      num = 1
      print "odd", num, den
    else:
      if fdict.has_key(den):
        break
      for prime in baseprimes:
        num2 = prime 
        den2 = den - num2 +1 
        if gd!=1:
          num /= gd
          den /= gd
          best = max(best,num2)
          break
  for key in flist:
    fdict[key]=num
#  print "\t\t\t\t",num, den
  return num#, fdict, best

def f4(k,dic):
  best, num, den, flist, fdict, bol = 0, 1, k, [], dic, True
  while den != 1:
#    print num,den
#    if num == 1:
    flist.append(den)
    if den&1==1:
      den = (den-1)>>1
      num = 1
    else:
      if fdict.has_key(den):
#        print 'this shouldn\'t happen...'
        num = fdict[den]
        den = 1
        break
      for num2 in baseprimes:
        den2 = den - num2 +1 
#        print num2,den2,"num,den2","den=",den
        if num2 >= den:
          num = den
          den = 1
          best = max(best,num2)
          break
        gd = gcd(num2, den2)
        if gd!=1:
          num /= gd
          den /= gd
          best = max(best,num2)
          break
#    print ""
  for key in flist:
    fdict[key]=num
#  print "\t\t\t\t",num, den
  return num, fdict, best
 
runningsum,tdict, baseprimes = 0, {1:1, 2:2, 3:1}, era2(40000000)
#for k in range(1,10):
#  print k, f4(k,tdict)[0]
#a = '''
import time
tStart = time.time()
for k in range(1,2000001):
  a,tdict,pRime = f4(k**3,tdict)
  runningsum += a
  print k,"("+str(k**3)+")","\t",len(tdict),"\t","Prime=",pRime
print "Run Time = " + str(time.time() - tStart)
print runningsum
#'''
#k, dic  = 0, {}
#while k < 100:
# k+=1
# print k, f2(k,dic)[0], f2(k**3,dic)[0]


#+-------------------------------------------------------------------+
#| testing whether the fraction class if faster than gcd function... |
#|                                                                   |
#|  f(k) ~ 13.8648200035 seconds                                     | 
#| f2(k) ~ 4.90715098381 seconds     so yeah, gcd was a lil' faster  |
#| f3(k) ~ 0.55958604813 seconds
#+-------------------------------------------------------------------+

#runningsum1= 0
#runningsum2= 0

#tstart1 = time.time()
#for k in range(1,301):
#  runningsum1 += f(k**3)
#print runningsum1
#print " f(k) ~ " + str(time.time() - tstart1)

#tstart2 = time.time()
#for k in range(1,301):
#  runningsum2 += f2(k**3)
#print runningsum2
#print "f2(k) ~ " + str(time.time() - tstart2)


