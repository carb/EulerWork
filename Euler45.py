#!/usr/bin/python
#lets try to just run through the numbers
#with a while loop and see if I can just
#reverse to check any polygonal properties.
from math import sqrt
def quadraticSolve(abclist):
  [a,b,c] = abclist
  ans1 = ((-1.0*b)+sqrt(b**2-4.0*a*c))/(2.0**a)
  return ans1 if ans1>=0 else ans2
def checkTri(num):
  n = quadraticSolve([1,1,-2.0*num])
  if n == int(n):
    return 1
  else:
    return 0
def checkPent(num,plist):
  #n = quadraticSolve([3,-1,-2.0*num])
  #if n == int(n):
  #  return 1
  #else:
  #  return 0
  return 1 if num in plist else 0
def checkHex(num):
  n = quadraticSolve([2,-1,-1.0*num])
  if n == int(n):
    return 1
  else:
    return 0
#pentlist =[]
#for i in range(60000):
#  pentlist.append((i*(3*i-1))/2)
#o,counter,c2 = 0,285,0
#while o==0:
#  counter += 1
#  c2 = counter*(counter+1)/2
#  if [checkPent(c2,pentlist),checkHex(c2)] == [1,1]:
#    o = 1
#  print counter
#print c2

def Tri(n):
  return n*(n+1)>>1

def Pent(n):
  return n*(n+n+n-1)>>1

def Hex(n):
  return n*((n<<1)-1)
import time


a,b,c = 286,166,144
status = False
tstart = time.time()
while status == False:
  a += 1
  t = Tri(a)
  h = Hex(c)
  if t<h:
    pass
  elif t==h:
    p = Pent(b)
    c += 1
    while t > p < h:
      b += 1
      p = Pent(b)
  else:
    c += 1
  if t==p==h:
    status = True
    print "Time =",(time.time()-tstart)
    print t,p,h
print a,b,c












