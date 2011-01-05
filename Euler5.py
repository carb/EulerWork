'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Brute force doesnt work!!

\>>> for num in range(10000000):
...   e = 0
...   for thang in range (1,21):
...     e += (num%thang)
...   if e == 0:
...     print num
... 
returned just zero


ok. so we have to check... 
if we take the prime factors of 2520 we get 2,2,2,3,3,5,7
how can we go from 
'1,2,3,4,5,6,7,8,9,10' -> '2,4,5,7,9' or '5,7,8,9'


10!
  2,2,2,2,2,2,2,2,3,3,3,3,5,5,7
=>2,2,2,          3,3,    5,  7

global primes
primes = [2]
global e
e = 0
global ans
ans = []

for num in range(10000)[2:]:
  e = 0
  for prime in primes:
    if num%prime > 0:
      e += 1
    if e == len(primes):
      primes += [num]

