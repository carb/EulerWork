import math
primes = [2]
e = 0
global ans
ans = 2
for num in range(10000)[2:]:
  e = 0
  for prime in primes:
    if num%prime > 0:
      e += 1
    if e == len(primes):
      primes += [num]
  if 600851475143%primes[-1] == 0:
    ans = primes[-1]
print ans

