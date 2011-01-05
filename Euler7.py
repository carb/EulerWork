global primes
primes = [2]
global e
e = 0
global ans
ans = []




for num in range(105000)[2:]:
  e = 0
  for prime in primes:
    if num%prime == 0:
      break
    elif prime == primes[-1]:
      primes += [num]

print len(primes)
print primes[10000:10002]

